from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import database

survey_router = Router()

class MenuSurvey(StatesGroup):
    name = State()
    phone_number = State()
    time_of_visit = State()
    rate_of_food = State()
    rate_of_cleaning = State()
    additional_review = State()

@survey_router.message(Command("stop"))
@survey_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за прохождение опроса!")

@survey_router.callback_query(F.data == "survey")
async def start_survey(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(MenuSurvey.name)
    await cb.message.answer("Как вас зовут?")


@survey_router.message(MenuSurvey.name)
async def process_phone_num(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(MenuSurvey.phone_number)
    await message.answer(f"Введите ваш номер телефона, {message.text}?")

@survey_router.message(MenuSurvey.phone_number)
async def process_time_of_visit(message: types.Message, state: FSMContext):
    phone_num = message.text
    if not phone_num.isdigit():
        await message.answer("Пожалуйста, верный номер телефона")
        return
    if not len(phone_num) == 10:
        await message.answer("Пожалуйста, верный номер телефона")
        return
    await state.update_data(phone_number=int(phone_num))
    await state.set_state(MenuSurvey.time_of_visit)
    await message.answer("Когда у вас был последний визит в нашем ресторане?")

@survey_router.message(MenuSurvey.time_of_visit)
async def process_rate_of_food(message: types.Message, state: FSMContext):
    await state.update_data(time_of_visit=message.text)
    await state.set_state(MenuSurvey.rate_of_food)
    await message.answer("Ваша оценка нашей еде?")

@survey_router.message(MenuSurvey.rate_of_food)
async def process_rate_of_cleaning(message: types.Message, state: FSMContext):
    await state.update_data(rate_of_food=message.text)
    await state.set_state(MenuSurvey.rate_of_cleaning)
    await message.answer("Ваша оценка нашей чистоте?")


@survey_router.message(MenuSurvey.rate_of_cleaning)
async def process_add_review(message: types.Message, state: FSMContext):
    await state.update_data(rate_of_cleaning=message.text)
    await state.set_state(MenuSurvey.additional_review)
    await message.answer("Оставьте отзыв о нашем заведении?")
    data = await state.get_data()
    print("!", data)



@survey_router.message(MenuSurvey.additional_review)
async def process_end(message: types.Message, state: FSMContext):
    await state.update_data(additional_review=message.text)
    data = await state.get_data()
    print("data:", data)
    await database.execute(
        "INSERT INTO survey (name, phone_number, time_of_visit, rate_of_food, rate_of_cleaning, additional_review) VALUES (?, ?, ?, ?, ?, ?)",
        (data.get("name"), data.get("phone_number"), data.get("time_of_visit"), data.get("rate_of_food"),
         data.get("rate_of_cleaning"), data.get("additional_review"))
    )
    await message.answer("Спасибо за пройденный опрос!")
    await state.clear()
