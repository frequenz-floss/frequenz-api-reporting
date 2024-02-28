import asyncio
from frequenz.client.reporting._client import Client
from frequenz.client.reporting._types import Metric
import grpc.aio as grpcaio



async def main():
    target="localhost:50051"

    client = Client(
        grpcaio.insecure_channel(target),  # or secure channel with credentials
    )

    microgrid_id = 10
    component_ids = [61]
    metrics = [Metric.DC_POWER]
    #resampling_options = None
    #include_options = None,
    print("wc")
    stream = await client.stream_microgrid_component_data(
        microgrid_id=microgrid_id,
        component_ids=component_ids,
        metrics=metrics,
    )
    print("wc0")
    async for fc in stream:
        print("wc1:", fc)
asyncio.run(main())
