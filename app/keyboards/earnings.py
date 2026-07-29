from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def earnings_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🔥 Фриланс"),
                KeyboardButton(text="📱 Онлайн-проекты")
            ],
            [
                KeyboardButton(text="🛒 Бизнес"),
                KeyboardButton(text="📈 Инвестиции")
            ],
            [
                KeyboardButton(text="⬅️ Назад")
            ]
        ],
        resize_keyboard=True
    )