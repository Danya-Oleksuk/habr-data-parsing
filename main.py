import asyncio
import aiohttp

from parser.config import BASE_URL, MAX_PAGES
from parser.fetcher import fetch_html
from parser.parser import parse_articles


async def process_page(session, page_num):
    url = BASE_URL.format(page_num)
    print(f"[INFO] Fetching: {url}")
    try:
        html = await fetch_html(session, url)
        await parse_articles(html)
    except Exception as e:
        print(f"[ERROR] Failed to process {url}: {e}")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [process_page(session, i) for i in range(1, MAX_PAGES + 1)]
        await asyncio.gather(*tasks)
    print("[DONE] All pages parsed.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[INFO] Parsing interrupted.")
