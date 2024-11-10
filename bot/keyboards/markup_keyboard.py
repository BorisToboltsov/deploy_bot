from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_markup_main_menu_keyboard(button_list: list) -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder_list = [
        [builder.add(types.KeyboardButton(text=button)) for button in button_list]
    ]
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def keyboard_remove() -> types.ReplyKeyboardRemove:
    return types.ReplyKeyboardRemove()
