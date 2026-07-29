import asyncio
import aiohttp


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://www.google.com",
            timeout=20
        ) as r:
            print(r.status)


asyncio.run(main())