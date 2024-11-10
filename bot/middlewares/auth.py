import json
import os
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from bot.view.auth import access_denied


class Auth(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:

        user = data.get("event_from_user")
        telegram_id = user.id
        first_name = user.first_name
        last_name = user.last_name
        username = user.username

        USER_SETTINGS = json.loads(os.getenv("USER_SETTINGS"))
        PROJECT_SETTINGS = json.loads(os.getenv("PROJECT_SETTINGS"))

        current_user_settings = USER_SETTINGS.get(str(telegram_id))
        access_project_settings = [{project: PROJECT_SETTINGS.get(project)} for project in current_user_settings.get('project')]

        if str(telegram_id) not in USER_SETTINGS:
            await access_denied(telegram_id)
        else:
            data["user_settings"] = current_user_settings
            data["project_settings"] = access_project_settings
            return await handler(event, data)
