from aiogram import types, Router
from aiogram.filters import Command
from pathlib import Path
from aiogram.filters import Command
from aiogram.types import FSInputFile
import random
import logging

pic_router = Router()

@pic_router.message(Command('picture_random'))
async def picture_random(message: types.Message):
    file_name = random.choice(list((Path(__file__).parent.parent / "images").iterdir()))
    file_path = Path(__file__).parent.parent / "images" / file_name
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)