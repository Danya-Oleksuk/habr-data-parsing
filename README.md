
# 📰 Habr Data Parser

An asynchronous web scraper that fetches articles from [Habr](https://habr.com/ru/hubs/python/articles/) using Python's `asyncio`, `aiohttp`, and `BeautifulSoup`.

## 📌 Description

This project is designed to parse Python-related articles from Habr, extract useful metadata, and store it in an Excel file (`parsed_data.xlsx`). It handles multiple pages concurrently and respects async I/O best practices.

---

## ✨ Features

- 🚀 Asynchronous HTTP requests with `aiohttp`
- 🔍 BeautifulSoup for HTML parsing
- 📥 Saves results into a structured Excel file
- 📊 Gathers title, link, article complexity level, and publication date
- ♻ Handles up to 50 pages concurrently

---

## 🔧 Technologies

- Python 3.10+
- `aiohttp`
- `asyncio`
- `request`
- `beautifulsoup4`
- `pandas`
- `lxml`
- `openpyxl`

---

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/Danya-Oleksuk/habr-data-parsing.git
cd habr-data-parsing
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the parser**

```bash
python main.py
```

The parser will collect data from pages of Habr's Python hub and save it to `parsed_data.xlsx`.
