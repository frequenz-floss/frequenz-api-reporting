import asyncio
from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime
from typing import AsyncIterator, List, Tuple

import grpc.aio as grpcaio
from frequenz.api.common.v1.metrics import metric_sample_pb2
from frequenz.api.common.v1.microgrid import microgrid_pb2
from frequenz.api.common.v1.pagination import pagination_params_pb2
from frequenz.api.reporting.v1 import reporting_pb2, reporting_pb2_grpc
from frequenz.client.common.metric import Metric
from google.protobuf.timestamp_pb2 import Timestamp

Sample = namedtuple("Sample", ["timestamp", "value"])
MetricSample = namedtuple(
    "MetricSample", ["timestamp", "microgrid_id", "component_id", "metric", "value"]
)


@dataclass(frozen=True)
class ComponentsDataPage:
    _data_pb: reporting_pb2.ListMicrogridComponentsDataResponse

    def is_empty(self) -> bool:
        if not self._data_pb.microgrids:
            return True
        if not self._data_pb.microgrids[0].components:
            return True
        if not self._data_pb.microgrids[0].components[0].metric_samples:
            return True
        return False

    def iterate_flat(self) -> dict:
        data = self._data_pb
        for mdata in data.microgrids:
            mid = mdata.microgrid_id
            for cdata in mdata.components:
                cid = cdata.component_id
                for msample in cdata.metric_samples:
                    ts = msample.sampled_at.ToDatetime()
                    met = Metric.from_proto(msample.metric).name
                    value = msample.sample.simple_metric.value
                    yield MetricSample(
                        timestamp=ts,
                        microgrid_id=mid,
                        component_id=cid,
                        metric=met,
                        value=value,
                    )

    @property
    def next_page_token(self) -> str:
        return self._data_pb.pagination_info.next_page_token


class ReportingClient:
    def __init__(self, service_address: str):
        self._grpc_channel = grpcaio.insecure_channel(service_address)
        self._stub = reporting_pb2_grpc.ReportingStub(self._grpc_channel)

    async def __aenter__(self) -> "ReportingClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def _components_data_iter(self, *args, **kwargs):
        async for page in self._iterate_components_data_pages(*args, **kwargs):
            for entry in page.iterate_flat():
                yield entry

    async def single_metric_iter(
        self, microgrid_id, component_id, metric, start_dt, end_dt, page_size=1000
    ):
        async for entry in self._components_data_iter(
            microgrid_components=[(microgrid_id, [component_id])],
            metrics=[metric],
            start_dt=start_dt,
            end_dt=end_dt,
            page_size=page_size,
        ):
            yield Sample(timestamp=entry.timestamp, value=entry.value)

    async def _iterate_components_data_pages(
        self,
        *,
        microgrid_components: list[tuple[int, list[int]]],
        metrics: list[Metric],
        start_dt: datetime,
        end_dt: datetime,
        page_size: int = 1000,
    ) -> AsyncIterator[ComponentsDataPage]:
        microgrid_components_pb = [
            microgrid_pb2.MicrogridComponentIDs(microgrid_id=mid, component_ids=cids)
            for mid, cids in microgrid_components
        ]

        def dt2ts(dt):
            ts = Timestamp()
            ts.FromDatetime(dt)
            return ts

        time_filter = reporting_pb2.TimeFilter(
            start=dt2ts(start_dt),
            end=dt2ts(end_dt),
        )

        list_filter = reporting_pb2.ListMicrogridComponentsDataRequest.ListFilter(
            time_filter=time_filter,
        )

        metrics_pb = [metric.to_proto() for metric in metrics]

        page_token = None

        while True:
            pagination_params = pagination_params_pb2.PaginationParams(
                page_size=page_size, page_token=page_token
            )

            response = await self.fetch_page(
                microgrid_components=microgrid_components_pb,
                metrics=metrics_pb,
                list_filter=list_filter,
                pagination_params=pagination_params,
            )
            if not response or response.is_empty():
                break

            yield response

            page_token = response.next_page_token
            if not page_token:
                break

    async def fetch_page(
        self, microgrid_components, metrics, list_filter, pagination_params
    ) -> ComponentsDataPage:
        try:
            response = await self._stub.ListMicrogridComponentsData(
                reporting_pb2.ListMicrogridComponentsDataRequest(
                    microgrid_components=microgrid_components,
                    metrics=metrics,
                    filter=list_filter,
                    pagination_params=pagination_params,
                )
            )
        except grpcaio.AioRpcError as e:
            print(f"RPC failed: {e}")
            return None
        return ComponentsDataPage(response)

    async def close(self):
        await self._grpc_channel.close()
