# License: MIT
# Copyright © 2024 Frequenz Energy-as-a-Service GmbH

"""The reporting API client."""

from typing import List

import grpc
from frequenz.api.reporting.v1 import (
    reporting_pb2,
    reporting_pb2_grpc,
)
from frequenz.channels import Receiver
from frequenz.client.base.grpc_streaming_helper import GrpcStreamingHelper

from _types import (
    Metric,
    MetricSample,
    MetricSampleVariant,
    SimpleMetricSample,
    AggregatedMetricSample,
    MicrogridComponentIDs,
    ComponentData,
    ComponentStateCode,
    ComponentErrorCode,
    ComponentState,
    PaginationParams,
    PaginationInfo,
    TimeFilter,
    ResamplingOptions,
    FilterOption,
    IncludeOptions,
    AggregationConfig,
    SimpleAggregatedMetricSample,
    ListFilter,
    MicrogridData,
    StreamFilter,
    AggregationListFilter,
    AggregatedResult,
    AggregatedStreamFilter,
)


class Client:
    """Reporting client."""

    def __init__(self, grpc_channel: grpc.aio.Channel) -> None:
        """Initialize the client.

        Args:
            grpc_channel: The gRPC channel to use for communication with the API.
        """

        self._stub = reporting_pb2_grpc.ReportingStub(grpc_channel)

        self._microgrid_component_data_streams: dict[
            tuple[MicrogridComponentIDs, Metric, StreamFilter],
            GrpcStreamingHelper[
                reporting_pb2.ReceiveMicrogridComponentsDataStreamResponse,
                tuple[int, ComponentData],
            ],
        ] = {}

    async def stream_microgrid_component_data(
        self,
        microgrid_id: int,  # MicrogridComponentIDs
        component_ids: List[int],
        metrics: List[Metric],  # Metric
        resampling_options: ResamplingOptions | None = None,  # StreamFilter
        include_options: IncludeOptions | None = None,
    ) -> Receiver[tuple[int, ComponentData]]:
        """Stream microgrid component data.

        Args:
            microgrid_id: The microgrid ID.
            component_ids: The component IDs.
            metrics: List metrics to stream.
            resampling_options: The optional resampling options.
            include_options: The optional include options.
        Returns:
            A receiver that yields tuples of the form (microgrid_component_id, component_data).
        """

        microgrid_components = MicrogridComponentIDs(
            microgrid_id=microgrid_id, component_ids=component_ids
        )

        filter = StreamFilter(
            resampling_options=resampling_options,
            include_options=include_options,
        )

        stream_key = tuple(
            tuple(microgrid_components) + tuple(metrics) + filter
        )

        if stream_key not in self._microgrid_component_data_streams:
            self._microgrid_component_data_streams[
                stream_key
            ] = GrpcStreamingHelper(
                f"reporting-{stream_key}",
                lambda: self._stub.ReceiveMicrogridComponentsDataStream(
                    reporting_pb2.ReceiveMicrogridComponentsDataStreamRequest(
                        microgrid_components=microgrid_components,
                        metrics=metrics,
                        filter=filter,
                    )
                ),
                lambda response: ComponentData.from_pb(
                    response.component_data
                ),
            )

        return self._microgrid_component_data_streams[
            stream_key
        ].new_receiver()
