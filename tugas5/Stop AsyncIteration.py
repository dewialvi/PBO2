import asyncio

async def my_coroutine():
    async for i in range(10):
        if i == 5:
            break
        print(i)
        await asyncio.sleep(1)

asyncio.run(my_coroutine())
