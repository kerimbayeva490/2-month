from aiogram import types, Router, F
from aiogram.filters import Command
from keyboards.keyboards import start_kb
from scapper.scrapper import Scrapper

start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    text = f'Hello {message.from_user.full_name} '
    await message.answer(text, reply_markup=start_kb())


@start_router.callback_query(F.data == 'parser')
async def parser(callback: types.CallbackQuery):
    await callback.answer()
    scrap = Scrapper()
    p_link = await scrap.get_links()
    for link in p_link:
        await callback.message.answer(link)