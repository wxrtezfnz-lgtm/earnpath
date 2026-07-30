from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)



def profile_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(
                    text="💰 Заработок"
                )
            ],

            [
                KeyboardButton(
                    text="🎓 Академия"
                )
            ]

        ],
        resize_keyboard=True
    )