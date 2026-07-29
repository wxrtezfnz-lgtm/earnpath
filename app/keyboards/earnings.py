from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def earnings_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🔥 Фриланс"),
                KeyboardButton(text="📱 Онлайн-проекты"),
            ],
            [
                KeyboardButton(text="🛒 Бизнес"),
                KeyboardButton(text="📈 Инвестиции"),
            ],
            [
                KeyboardButton(text="🔙 Назад"),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выбери направление 👇",
    )


def freelance_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="💻 Копирайтинг"),
                KeyboardButton(text="🎨 Дизайн"),
            ],
            [
                KeyboardButton(text="👨‍💻 Программирование"),
                KeyboardButton(text="🤖 AI-услуги"),
            ],
            [
                KeyboardButton(text="🔙 Назад"),
            ],
        ],
        resize_keyboard=True,
    )


def online_projects_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📢 Telegram-проекты"),
            ],
            [
                KeyboardButton(text="🎬 Создание контента"),
            ],
            [
                KeyboardButton(text="📦 Цифровые продукты"),
            ],
            [
                KeyboardButton(text="🔙 Назад"),
            ],
        ],
        resize_keyboard=True,
    )


def business_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🛒 Продажи"),
            ],
            [
                KeyboardButton(text="🌐 E-commerce"),
            ],
            [
                KeyboardButton(text="⚙️ Услуги"),
            ],
            [
                KeyboardButton(text="🔙 Назад"),
            ],
        ],
        resize_keyboard=True,
    )


def investments_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📚 Обучение"),
            ],
            [
                KeyboardButton(text="🔙 Назад"),
            ],
        ],
        resize_keyboard=True,
    )