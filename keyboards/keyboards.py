from aiogram import types


def start_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш Инстаграмм", url="https://instagram.com")
            ],
            [
                types.InlineKeyboardButton(text="Наше меню", callback_data="menu")
            ],
            [
                types.InlineKeyboardButton(text='Пройти опросник', callback_data="survey")
            ]
        ]
    )
    return kb


def menu_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Супы")
            ],
            [
                types.KeyboardButton(text="Пиццы")
            ],
            [
                types.KeyboardButton(text="Роллы")
            ]
        ]
    )
    return kb