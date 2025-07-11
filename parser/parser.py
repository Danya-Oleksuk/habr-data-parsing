from bs4 import BeautifulSoup
from parser.writer import write_to_excel

async def parse_articles(html: str):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('article', class_='tm-articles-list__item')

    for article in articles:
        title_tag = article.find('a', class_='tm-title__link')
        if not title_tag:
            continue

        title = title_tag.text.strip()
        link = "https://habr.com" + title_tag.get('href', '')
        time = article.find('a', class_='tm-article-datetime-published').text.strip()
        level_tag = article.find('span', class_='tm-article-complexity__label')
        level = level_tag.text.strip() if level_tag else '-'

        await write_to_excel([title, link, level, time])
