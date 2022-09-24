#!/usr/bin/python3
import time
import random

import async_module

NO_TASKS = 10

def consumer(n: int):
    """
    This routine implements a consumer. 
    This can be a function waiting for results from an I/O operation.
    """
    print(f'Consumer {n} start calling Producer to get data.')
    res = yield async_module.Task(producer(n))
    print(f'Consumer {n} got data. Data: {res}')

def producer(n: int) -> str:
    """
    This routine implements a producer. 
    This can be an I/O operation that takes time.
    """
    wait_time = random.randint(0,10)
    print(f'Producer {n} received call to produce data. Data to be ready in {wait_time} seconds.')
    yield async_module.Task(async_module.sleep(wait_time))
    print(f'Producer {n} data ready.')
    return f'{n}-data'

def main():
    loop = async_module.EventLoop()
    for i in range(NO_TASKS):
        loop.create_task(consumer(i))

    start = time.perf_counter()
    loop.run_until_complete()
    print(f'Process done in {time.perf_counter() - start} seconds')

if __name__ == '__main__':
    main()
