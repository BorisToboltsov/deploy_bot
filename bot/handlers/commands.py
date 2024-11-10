from typing import NoReturn

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from bot.states.choice_project import FSMProject
from bot.view.command_start import change_project

router_commands = Router()


@router_commands.message(Command("start"))
async def commands_start(
    message: types.Message, user_settings: dict, project_settings: list, state: FSMContext) -> NoReturn:
    await state.set_state(FSMProject.choice_project)
    await change_project(message.from_user.id, user_settings.get("project"))
