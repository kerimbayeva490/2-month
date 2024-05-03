from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import menu_kb

menu_router = Router()

@menu_router.callback_query(F.data == 'menu')
async def menu(callback: types.CallbackQuery):
    await callback.message.answer(text="Что пожелаете", reply_markup=menu_kb())


@menu_router.message(F.text.lower() == "супы")
async def show_pizza(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Вот супы, которые мы вам предлагаем", reply_markup=kb)


@menu_router.message(F.text.lower() == "пицца")
async def show_pizza(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Вот пиццы, которые мы вам предлагаем", reply_markup=kb)


@menu_router.message(F.text.lower() == "роллы")
async def show_pizza(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Вот роллы, которые мы вам предлагаем", reply_markup=kb)



