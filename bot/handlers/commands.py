from typing import NoReturn

from aiogram import Router, types
from aiogram.filters import Command

router_commands = Router()


@router_commands.message(Command("start"))
async def commands_start(message: types.Message) -> NoReturn:
    print(1)
