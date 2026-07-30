from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


def design_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(
                    text="🎨 Урок 1"
                )
            ],

            [
                KeyboardButton(
                    text="🌈 Урок 2"
                )
            ],

            [
                KeyboardButton(
                    text="🖼 Урок 3"
                )
            ],

            [
                KeyboardButton(
                    text="⬅️ Назад"
                )
            ]

        ],
        resize_keyboard=True
    )



def lesson_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(
                    text="✅ Завершить урок"
                )
            ]

        ],
        resize_keyboard=True
    )



def next_lesson_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(
                    text="➡️ Следующий урок"
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