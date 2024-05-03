from aiogram import types, Router
from aiogram.filters import Command

echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    chat_id = message.from_user.id
    text = message.text
    await message.answer(chat_id=chat_id, text=text)
