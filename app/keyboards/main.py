from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


def main_keyboard():

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
            ],
            [
                KeyboardButton(
                    text="👤 Профиль"
                )
            ]
        ],
        resize_keyboard=True
    )