import os
import asyncio
import pandas as pd
from parser.config import EXCEL_FILE

lock = asyncio.Lock()

async def write_to_excel(data: list):
    async with lock:
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE)
        else:
            df = pd.DataFrame(columns=['Заголовок статьи', 'Ссылка на статью', 'Уровень статьи (если есть)', 'Дата выхода статьи'])

        new_row = pd.DataFrame([data], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
