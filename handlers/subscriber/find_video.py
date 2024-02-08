from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from data.constans import INVALID_INPUT, NOTHING_FOUND, ENTER_COMMAND
from database.get_result_from_database import get_result_from_database
from filters.is_private import IsChatPrivate
from filters.is_subscribed import IsSubscribed
from data.data_buttons import Button

router = Router()


class StagesFindingVideos(StatesGroup):
    code = State()


@router.message(IsChatPrivate(), F.text == Button.FIND_VIDEO.value, IsSubscribed())
async def command_find_video(message: types.Message, state: FSMContext):
    await message.answer("Введи код, чтобы найти фильм или сериал")
    await state.set_state(StagesFindingVideos.code)


@router.message(IsChatPrivate(), StateFilter(StagesFindingVideos.code), IsSubscribed())
async def find_video_by_code(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer(INVALID_INPUT)
        return

    results = await get_result_from_database(message.text)
    if len(results) == 0:
        await message.answer(NOTHING_FOUND)
        await message.answer(ENTER_COMMAND)
    else:
        for row in results:
            await message.answer_video(row[0])
    await state.clear()

