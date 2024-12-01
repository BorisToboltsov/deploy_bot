import asyncio
import os
import datetime
import subprocess
from typing import NoReturn
from aiogram.fsm.context import FSMContext


from bot.view.load_database import load_database_complete_view


async def load_database(db_name: str, telegram_id: int, state: FSMContext) -> NoReturn:
    reset_master = f'mysql -u {os.getenv("USER_BACKUP")} -p{os.getenv("PASSWORD_BACKUP")} -Bse "RESET MASTER;"'
    # os.system(reset_master)
    subprocess.run(reset_master)

    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    load = f'mysql -u {os.getenv("USER_BACKUP")} -p{os.getenv("PASSWORD_BACKUP")} {db_name} < {os.getenv("PATH_TO_BACKUP")}/{db_name}_{current_date}.sql'
    # os.system(load)
    subprocess.run(load)

    await load_database_complete_view(telegram_id)
    await state.update_data(load_active=False)
