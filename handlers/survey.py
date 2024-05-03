from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

survey_router = Router()

class MenuSurvey(StatesGroup):
    name = State()
    phone_number = State()
    time_of_visit = State()
    rate_of_food = State()
    rate_of_cleaning = State()
    additional_review = State()

@survey_router.callback_query(F.data == "survey")
async def start_survey(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(MenuSurvey.name)
    await cb.message.answer("Как вас зовут?")


@survey_router.message(MenuSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(MenuSurvey.phone_number)
    await message.answer(f"Введите ваш номер телефона, {message.text}?")

@survey_router.message(MenuSurvey.phone_number)
async def process_age(message: types.Message, state: FSMContext):
    phone_num = message.text
    if not phone_num.isdigit():
        await message.answer("Пожалуйста, верный номер телефона")
        return
    if not len(phone_num) == 10:
        await message.answer("Пожалуйста, верный номер телефона")
        return
    await state.update_data(age=int(phone_num))
    await state.set_state(MenuSurvey.time_of_visit)
    await message.answer("Когда у вас был последний визит в нашем ресторане?")

@survey_router.message(MenuSurvey.time_of_visit)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(MenuSurvey.rate_of_food)
    await message.answer("Ваша оценка нашей еде?")

@survey_router.message(MenuSurvey.rate_of_food)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(MenuSurvey.rate_of_cleaning)
    await message.answer("Ваша оценка нашей чистоте?")


@survey_router.message(MenuSurvey.rate_of_cleaning)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(MenuSurvey.additional_review)
    await message.answer("Оставьте отзыв о нашем заведении?")



@survey_router.message(MenuSurvey.additional_review)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer("Спасибо за пройденный опрос!")