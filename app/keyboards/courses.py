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
                    text="🎨 Урок 5"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Урок 6"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Урок 7"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Урок 8"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Урок 9"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Урок 10"
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