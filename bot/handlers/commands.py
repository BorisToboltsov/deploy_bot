from typing import NoReturn

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router_commands = Router()

@router_commands.message(Command("start"))
async def commands_start(message: types.Message) -> NoReturn:
    print(1)
