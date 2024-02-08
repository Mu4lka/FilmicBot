import asyncio

from aiogram import Bot

from database.create_database import create_database
from handlers import common
from handlers.admin import add_video
from handlers.subscriber import find_video
from loader import dispatcher, bot
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify


async def on_startup(bot: Bot):
    await set_default_commands(bot)
    await on_startup_notify(bot)


def include_routers():
    routers = [common.router, find_video.router, add_video.router, ]
    for router in routers:
        dispatcher.include_router(router)


async def main():
    await create_database()
    await on_startup(bot)
    include_routers()
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
