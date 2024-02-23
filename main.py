import asyncio
import aiohttp
from bs4 import BeautifulSoup

import pandas as pd
import os


async def write_data(data):
    file_name = 'parsed_data.xlsx'
    
    async with asyncio.Lock():
        if os.path.isfile(file_name):
            existing_data = pd.read_excel(file_name)
        else:
            existing_data = pd.DataFrame(columns=['Заголовок статьи', 'Ссылка на статью', 'Уровень статьи (если есть)', 'Дата выхода статьи'])
        
        new_df = pd.DataFrame([data], columns=['Заголовок статьи', 'Ссылка на статью', 'Уровень статьи (если есть)', 'Дата выхода статьи'])
        updated_data = pd.concat([existing_data, new_df], ignore_index=True)
        updated_data.to_excel(file_name, index=False)

           
async def parse(session, url, headers):
    async with session.get(url, headers=headers) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find_all('article', class_ = 'tm-articles-list__item')
            
        for page in data:
            title = page.find('a', class_ ='tm-title__link').text
            link = "https://habr.com" + page.find('a', class_ ='tm-title__link').get('href')
            time = page.find('a', class_ ='tm-article-datetime-published tm-article-datetime-published_link').text
            level = page.find('span', class_ = 'tm-article-complexity__label')
            level = level.text.strip() if level else '-'
            await write_data([title, link, level, time])

        
async def main():
    async with aiohttp.ClientSession() as session:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
        
        from_what_to_what = [(1,25), (25, 49), (49, 51)]
        
        for start, end in from_what_to_what:
            tasks = []
            for i in range(start, end):
                url = f'https://habr.com/ru/hubs/python/articles/page{i}/'
                task = asyncio.create_task(parse(session, url, headers))
                tasks.append(task)
            
            await asyncio.gather(*tasks)
        
        print(f"Work is done.")
        
        
        
if  __name__ == '__main__':
    asyncio.run(main())