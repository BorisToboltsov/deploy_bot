import os
import datetime
from typing import NoReturn


async def load_database(db_name: str) -> NoReturn:
    reset_master = f'mysql -u {os.getenv("USER_BACKUP")} -p{os.getenv("PASSWORD_BACKUP")} -Bse "RESET MASTER;"'
    os.system(reset_master)

    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    load = f'mysql -u {os.getenv("USER_BACKUP")} -p{os.getenv("PASSWORD_BACKUP")} {db_name} < {os.getenv("PATH_TO_BACKUP")}/{db_name}_{current_date}.sql'
    os.system(load)
