from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)



def academy_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(
                    text="🎨 Дизайн"
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