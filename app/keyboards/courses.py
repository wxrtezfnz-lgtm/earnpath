from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def design_lessons_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🎨 Урок 1"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Урок 2"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Урок 3"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Урок 4"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Дизайн"
                )
            ]
        ],
        resize_keyboard=True
    )