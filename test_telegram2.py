import asyncio
import aiohttp
import socket
import ssl


async def main():

    ssl_context = ssl.create_default_context()

    connector = aiohttp.TCPConnector(
        family=socket.AF_INET,
        ssl=ssl_context,
        force_close=True
    )

    async with aiohttp.ClientSession(
        connector=connector
    ) as session:

        async with session.get(
            "https://api.telegram.org",
            timeout=30
        ) as response:

            print(response.status)
            print(await response.text())


asyncio.run(main())