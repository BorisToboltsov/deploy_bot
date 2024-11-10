from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_builder_inline_keyboard(
    button_name_list: list, line: int
) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for button_name in button_name_list:
        builder_list = [
            [
                builder.add(
                    types.InlineKeyboardButton(
                        text=button_name.split(" ")[0],
                        callback_data=button_name,
                    )
                )
            ],
        ]
    builder.adjust(line)
    return builder.as_markup(resize_keyboard=True)
