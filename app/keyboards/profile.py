from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def profile_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="👤 Профиль"
                )
            ],
            [
                KeyboardButton(
                    text="💰 Заработок"
                )
            ]
        ],
        resize_keyboard=True
    )