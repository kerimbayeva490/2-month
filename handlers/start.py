from aiogram import types, Router
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш Инстаграмм", url="https://instagram.com")
            ],
            [
                types.InlineKeyboardButton(text="Наше меню", callback_data="menu")
            ]
        ]
    )
    text = f'Hello {message.from_user.full_name} '
    await message.answer(text, reply_markup=kb)

