from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def make_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for item in items:
        builder.row(KeyboardButton(text=item))
    markup = builder.as_markup()
    markup.resize_keyboard = True
    return markup
