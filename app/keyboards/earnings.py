from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def earnings_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🔥 Фриланс")
            ],
            [
                KeyboardButton(text="📱 Онлайн-проекты")
            ],
            [
                KeyboardButton(text="🛒 Бизнес")
            ],
            [
                KeyboardButton(text="📈 Инвестиции")
            ],
        ],
        resize_keyboard=True
    )


def freelance_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🎨 Дизайн")
            ],
            [
                KeyboardButton(text="💻 Программирование")
            ],
            [
                KeyboardButton(text="✍️ Копирайтинг")
            ],
            [
                KeyboardButton(text="🤖 AI-услуги")
            ],
            [
                KeyboardButton(text="💰 Заработок")
            ],
        ],
        resize_keyboard=True
    )