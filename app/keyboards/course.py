from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def design_lessons_keyboard():
    buttons = []

    for i in range(1, 11):
        buttons.append(
            [
                KeyboardButton(
                    text=f"🎨 Урок {i}"
                )
            ]
        )

    buttons.append(
        [
            KeyboardButton(text="💰 Заработок")
        ]
    )

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )