from aiogram import types, Router
from aiogram.filters import Command
import logging

echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    logging.info(message)
    await message.answer(message.text)
