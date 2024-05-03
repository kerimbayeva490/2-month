from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from keyboards.keyboards import menu_kb
from config import database

menu_router = Router()


@menu_router.callback_query(F.data == 'menu')
async def menu(callback: types.CallbackQuery):
    await callback.message.answer(text="Что пожелаете", reply_markup=menu_kb())


types_of_meal = ['супы', 'роллы', 'пиццы']
@menu_router.message(F.text.lower().in_(types_of_meal))
async def show_horror(message: types.Message):
    type_of_meal = message.text.lower()
    print(type_of_meal)
    kb = types.ReplyKeyboardRemove()
    data = await database.fetch(
        """
        SELECT meals.* FROM meals 
        JOIN types ON meals.type_id = types.id
        WHERE types.name = ?
        """,
        (type_of_meal,),
        fetch_type='all'
    )
    if not data:
        await message.answer('По вашему запросу ничего не найдено', reply_markup=kb)
    await message.answer(f'Все наши блюда типа {types_of_meal}:')
    for meal in data:
        price = meal['price']
        name = meal['name']
        photo = types.FSInputFile(meal['picture'])
        await message.answer_photo(
            photo=photo,
            caption=f'Название блюда: {name}\nЦена: {price} сом'
        )



