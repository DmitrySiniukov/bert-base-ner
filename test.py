# SuperFastPython.com
# hello world program for asyncio
import asyncio
import time


async def custom_coroutine(arg1, arg2):
    print('Start')
    await asyncio.sleep(5)
    print('end')
    return arg1 + arg2


async def custom_coroutine2(arg1, arg2):
    print('start 2')
    await asyncio.sleep(5.5)
    print('end 2')
    return arg1 + arg2


# define a coroutine
async def main():
    # report a message
    print('...')
    task = asyncio.create_task(custom_coroutine(1, 2))
    task2 = asyncio.create_task(custom_coroutine2(2, 3))
    print('Hello world')
    results = await asyncio.wait([task, task2])
    print('Hello world')
    print(results)
    input()

    results = await asyncio.gather(custom_coroutine(1, 2), custom_coroutine2(2, 3))
    print(results)
    input()


if __name__ == '__main__':
    # execute the coroutine
    asyncio.run(main())
ф