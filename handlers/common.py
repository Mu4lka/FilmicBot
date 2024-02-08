from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from data.config import GROUP_CHAT_ID
from data.constans import HELLO_BOT
from filters.is_admin import IsAdmin
from filters.is_private import IsChatPrivate
from filters.is_subscribed import IsSubscribed
from data.data_buttons import admin_buttons, subscriber_buttons, Button
from keyboards.make_keyboard import make_keyboard

router = Router()


@router.message(IsChatPrivate(), F.text == Button.CANCEL.value, IsSubscribed())
async def command_cancel(message: types.Message, state: FSMContext):
    await message.answer("Отменено")
    await state.clear()


@router.message(IsChatPrivate(), Command("start"))
async def command_start(message: types.Message):
    markup = ReplyKeyboardBuilder().as_markup()
    if await IsAdmin().__call__(message):
        markup = make_keyboard(admin_buttons)
    elif await IsSubscribed().__call__(message):
        markup = make_keyboard(subscriber_buttons)
    else:
        return
    await message.answer(f"Привет {message.from_user.full_name}, {HELLO_BOT}", reply_markup=markup)


@router.message(IsChatPrivate(), Command("help"))
async def command_help(message: types.Message):
    await message.answer(f"Нужна помощь? задай вопрос в чат {GROUP_CHAT_ID}")


@router.message(IsChatPrivate(), Command("info_bot"))
async def command_info_bot(message: types.Message):
    await message.answer(f"Creator: @Mu4lka")

