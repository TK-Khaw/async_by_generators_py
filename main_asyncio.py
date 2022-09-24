#!/usr/bin/python3
import time
import random
import asyncio

NO_TASKS = 10

async def consumer(n: int):
    """
    This routine implements a consumer. 
    This can be a function waiting for results from an I/O operation.
    """
    print(f'Consumer {n} start calling Producer to get data.')
    res = await producer(n)
    print(f'Consumer {n} got data. Data: {res}')

async def producer(n: int) -> str:
    """
    This routine implements a producer. 
    This can be an I/O operation that takes time.
    """
    wait_time = random.randint(0,10)
    print(f'Producer {n} received call to produce data. Data to be ready in {wait_time} seconds.')
    await asyncio.sleep(wait_time)
    print(f'Producer {n} data ready.')
    return f'{n}-data'

async def main():
    tasks = []
    for i in range(NO_TASKS):
        tasks.append(asyncio.create_task(consumer(i)))

    start = time.perf_counter()
    for task in tasks:
        await task
    print(f'Process done in {time.perf_counter() - start} seconds')

if __name__ == '__main__':
    asyncio.run(main())
