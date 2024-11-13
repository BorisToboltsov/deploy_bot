import os
from pprint import pprint
from typing import NoReturn

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.states.choice_project import FSMProject
from bot.view.command_start import change_project
from bot.view.openproject import work_packages_view
from bot.view.project import (
    checkout_view,
    project_settings_view,
    pull_view,
    reset_view,
    set_checkout_view, status_view,
)
from openproject.api.work_package import ApiWorkPackage
from services.git_work import GitObject

router_message = Router()


@router_message.callback_query(FSMProject.choice_project)
async def choice_project_handler(
    callback_query: CallbackQuery, project_settings: dict, state: FSMContext
) -> NoReturn:
    project = project_settings.get(callback_query.data)
    git_object = GitObject(project.get("path"))
    await state.set_state(FSMProject.set_project)
    await state.update_data(git_object=git_object)
    await project_settings_view(callback_query.from_user.id)


@router_message.message(F.text == "Pull", FSMProject.set_project)
async def pull_handler(
    message: Message, user_settings: dict, project_settings: dict, state: FSMContext
) -> NoReturn:
    data = await state.get_data()
    git_object = data.get("git_object")
    if git_object is None:
        await state.set_state(FSMProject.choice_project)
        await change_project(message.from_user.id, user_settings.get("project"))
    else:
        response = await git_object.pull()
        await pull_view(message.from_user.id, response)


@router_message.message(F.text == "Checkout", FSMProject.set_project)
async def checkout_handler(
    message: Message, user_settings: dict, project_settings: dict, state: FSMContext
) -> NoReturn:
    data = await state.get_data()
    git_object = data.get("git_object")
    if git_object is None:
        await state.set_state(FSMProject.choice_project)
        await change_project(message.from_user.id, user_settings.get("project"))
    else:
        await state.set_state(FSMProject.set_checkout)
        await checkout_view(message.from_user.id)


@router_message.message(F.text, FSMProject.set_checkout)
async def set_checkout_handler(
    message: Message, user_settings: dict, project_settings: dict, state: FSMContext
) -> NoReturn:
    data = await state.get_data()
    git_object = data.get("git_object")
    if git_object is None:
        await state.set_state(FSMProject.choice_project)
        await change_project(message.from_user.id, user_settings.get("project"))
    else:
        response = await git_object.checkout(message.text)
        await state.set_state(FSMProject.set_project)
        await set_checkout_view(message.from_user.id, response, message.text)


@router_message.message(F.text == "Reset", FSMProject.set_project)
async def checkout_handler(
    message: Message, user_settings: dict, project_settings: dict, state: FSMContext
) -> NoReturn:
    data = await state.get_data()
    git_object = data.get("git_object")
    if git_object is None:
        await state.set_state(FSMProject.choice_project)
        await change_project(message.from_user.id, user_settings.get("project"))
    else:
        response = await git_object.reset()
        await reset_view(message.from_user.id, response)


@router_message.message(F.text == "Выбрать проект")
async def choice_project_handler(
    message: Message, user_settings: dict, project_settings: dict, state: FSMContext
) -> NoReturn:
    await state.set_state(FSMProject.choice_project)
    await change_project(message.from_user.id, user_settings.get("project"))


@router_message.message(F.text == "Status", FSMProject.set_project)
async def status_handler(
    message: Message, user_settings: dict, project_settings: dict, state: FSMContext
) -> NoReturn:
    data = await state.get_data()
    git_object = data.get("git_object")
    if git_object is None:
        await state.set_state(FSMProject.choice_project)
        await change_project(message.from_user.id, user_settings.get("project"))
    else:
        response = await git_object.status()
        await status_view(message.from_user.id, response)


@router_message.message(F.text == "Задачи", FSMProject.set_project)
async def status_handler(
    message: Message, user_settings: dict, project_settings: dict, state: FSMContext
) -> NoReturn:
    openproject_user_id = user_settings.get("openproject").get("id")
    api_work_package = ApiWorkPackage()
    response = await api_work_package.get_work_package_by_user(openproject_user_id)
    work_packages = response.get('_embedded').get('elements')
    message_view = ''
    for i, work_package in enumerate(work_packages, 1):
        id = work_package.get('id')
        subject = work_package.get('subject')
        link = f"{os.getenv("URL_WORK_PACKAGE")}{id}"
        message_view += f'{i}: <a href="{link}">{subject}</a>\n'
    await work_packages_view(message.from_user.id, message_view)
