import asyncio
import logging
import os
import random

from aiogram import Bot, Dispatcher, types
from random import choice
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from aiogram.filters import Command
from aiogram.types import FSInputFile

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def start(message: types.Message):
    text = f'Hello {message.from_user.full_name} '
    await message.answer(text)


@dp.message(Command('myinfo'))
async def info(message: types.Message):
    text = (f'Your id is {message.from_user.id}\n'
            f'Your username is {message.from_user.username}\n'
            f'Your fullname is {message.from_user.full_name}\n')
    await message.answer(text=text)


@dp.message(Command('picture_random'))
async def picture_random(message: types.Message):
    file_name = random.choice(list((Path(__file__).parent / "Images").iterdir()))
    file_path = Path(__file__).parent.parent / "Images" / file_name
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)


@dp.message()
async def echo(message: types.Message):
    chat_id = message.from_user.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
