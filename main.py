import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from handlers.start import start_router
from handlers.info import info_router
from handlers.random_pic import pic_router
from handlers.echo import echo_router
from handlers.menu import menu_router

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(pic_router)
    dp.include_router(menu_router)
    # в самом конце
    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
