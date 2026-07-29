from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def design_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📚 Уроки дизайна"),
                KeyboardButton(text="💼 Поиск клиентов"),
            ],
            [
                KeyboardButton(text="🧰 Инструменты"),
            ],
            [
                KeyboardButton(text="💰 Заработок"),
            ],
        ],
        resize_keyboard=True
    )