import asyncio
import os
import datetime
import subprocess
from typing import NoReturn
from aiogram.fsm.context import FSMContext


from bot.view.load_database import load_database_complete_view, load_database_stdout_view


async def load_database(db_name: str, telegram_id: int, state: FSMContext) -> NoReturn:
    reset_master = f'mysql -u {os.getenv("USER_BACKUP")} -p{os.getenv("PASSWORD_BACKUP")} -Bse "RESET MASTER;"'
    # os.system(reset_master)
    t1 = subprocess.run(["mysql", "-u", os.getenv("USER_BACKUP"), f"-p{os.getenv("PASSWORD_BACKUP")}", "-Bse", "RESET MASTER;"], stdout=subprocess.PIPE)

    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    command = [
        'mysql',
        '-u', os.getenv("USER_BACKUP"),
        '-p' + os.getenv("PASSWORD_BACKUP"),
        db_name
        ]
    load = f'mysql -u {os.getenv("USER_BACKUP")} -p{os.getenv("PASSWORD_BACKUP")} {db_name} < {os.getenv("PATH_TO_BACKUP")}/{db_name}_{current_date}.sql'
    # os.system(load)
    # t2 = subprocess.run(["mysql", "-u", os.getenv("USER_BACKUP"), f"-p{os.getenv("PASSWORD_BACKUP")}", db_name, "<", f"{os.getenv("PATH_TO_BACKUP")}/{db_name}_{current_date}.sql"], stdout=subprocess.PIPE)
    # await load_database_stdout_view(telegram_id, t2.stdout.decode('utf-8')[:2500])
    with open(f'{os.getenv("PATH_TO_BACKUP")}/{db_name}_{current_date}.sql', 'r') as file:
        # process = subprocess.run(
        # command,
        # stdin = file,
        #         )

        process = await asyncio.create_subprocess_exec(
             *command,

        stdin = file,

        stdout = asyncio.subprocess.PIPE,

        stderr = asyncio.subprocess.PIPE
                    )
         # Ожидаем завершения процесса
        stdout, stderr = await process.communicate()

    await load_database_complete_view(telegram_id)
    await state.update_data(load_active=False)
