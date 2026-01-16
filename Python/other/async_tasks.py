import asyncio
from time import time

async def task_one():
    print('start task one')
    await asyncio.sleep(1)
    print('stop task one')
    
async def task_two():
    print('start task two')
    await asyncio.sleep(2)
    print('stop task two')
    
async def task_three():
    print('start task three')
    await asyncio.sleep(3)
    print('stop task three')
    
async def main():
    await asyncio.gather(task_one(), task_two(), task_three())
    
if __name__ == '__main__':
    start = time()
    asyncio.run(main())
    print(time()- start)
    