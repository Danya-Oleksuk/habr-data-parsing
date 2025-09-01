import aiohttp
from parser.config import HEADERS


async def fetch_html(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url, headers=HEADERS) as response:
        return await response.text()
