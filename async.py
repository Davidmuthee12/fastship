import time
import asyncio

from rich import print


async def endpoint(route: str) -> str:
    print(f">> handling {route}")

    # emulate database delay
    await asyncio.sleep(1)

    print(f"<< response {route}")
    return route


async def server():
    # Run test request
    tests = (
        "Get /shipment?id=1",
        "Patch /shipment?id=4",
        "Get /shipment?id=3",
    )

    start = time.perf_counter()

    requests = [asyncio.create_task(endpoint(route)) for route in tests]

    done, pending = await asyncio.wait(requests)

    for task in done:
        print("Result:", task.result())

    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f}s")


# Run Server
asyncio.run(server())
