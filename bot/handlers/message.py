from typing import NoReturn

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.states.choice_project import FSMChoiceProject

router_message = Router()


@router_message.callback_query(FSMChoiceProject.choice_project)
async def choice_transport_handler(
    callback_query: CallbackQuery, project_settings: list, state: FSMContext
) -> NoReturn:
    print(project_settings)
    print(callback_query.data)

