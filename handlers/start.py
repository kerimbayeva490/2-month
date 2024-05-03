from aiogram import types, Router
from aiogram.filters import Command
from keyboards.keyboards import start_kb

start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    text = f'Hello {message.from_user.full_name} '
    await message.answer(text, reply_markup=start_kb())

