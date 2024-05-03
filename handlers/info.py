from aiogram import types, Router
from aiogram.filters import Command

info_router = Router()

@info_router.message(Command('myinfo'))
async def info(message: types.Message):
    text = (f'Your id is {message.from_user.id}\n'
            f'Your username is {message.from_user.username}\n'
            f'Your fullname is {message.from_user.full_name}\n')
    await message.answer(text=text)