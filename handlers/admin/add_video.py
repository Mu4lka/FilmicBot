from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from data.constans import INVALID_INPUT
from database.add_video_in_database import add_video_in_database
from filters.is_admin import IsAdmin
from filters.is_private import IsChatPrivate
from filters.is_subscribed import IsSubscribed
from data.data_buttons import Button

router = Router()


class StagesAddingVideo(StatesGroup):
    primary = State()
    code = State()
    file_id = State()


@router.message(IsChatPrivate(), F.text == Button.ADD_VIDEO.value, IsSubscribed(), IsAdmin())
async def command_add_video(message: types.Message, state: FSMContext):
    await message.answer("Отправь мне видео или его код")
    await state.set_state(StagesAddingVideo.primary)


@router.message(IsChatPrivate(), StateFilter(StagesAddingVideo.primary), IsSubscribed(), IsAdmin())
async def take_code_or_video_file_id(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(code=message.text)
        await message.answer("Отправь видео")
        await state.set_state(StagesAddingVideo.file_id)
    elif message.video:
        await state.update_data(file_id=message.video.file_id)
        await message.answer("Отправь код")
        await state.set_state(StagesAddingVideo.code)
    else:
        await message.answer(INVALID_INPUT)


@router.message(IsChatPrivate(), StateFilter(StagesAddingVideo.code), IsSubscribed(), IsAdmin())
async def take_code(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer(INVALID_INPUT)
        return

    await state.update_data(code=message.text)
    await commit_data(message, state)


@router.message(IsChatPrivate(), StateFilter(StagesAddingVideo.file_id), IsSubscribed(), IsAdmin())
async def take_file_id(message: types.Message, state: FSMContext):
    if not message.video:
        await message.answer(INVALID_INPUT)
        return

    await state.update_data(file_id=message.video.file_id)
    await commit_data(message, state)


async def commit_data(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await add_video_in_database(user_data['code'], user_data['file_id'])
    await message.answer(f"Видео под кодом {user_data['code']} успешно добавлено")
    await state.clear()
