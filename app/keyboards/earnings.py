from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def earnings_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔥 Фриланс",
                    callback_data="earn_freelance"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📱 Онлайн-проекты",
                    callback_data="earn_online"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛒 Бизнес",
                    callback_data="earn_business"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📈 Инвестиции",
                    callback_data="earn_invest"
                )
            ]
        ]
    )


def freelance_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💼 Найти клиентов",
                    callback_data="freelance_clients"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🧠 Какие навыки нужны",
                    callback_data="freelance_skills"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🚀 Первые шаги",
                    callback_data="freelance_start"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_earnings"
                )
            ]
        ]
    )


def online_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🤖 AI проекты",
                    callback_data="online_ai"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢 Telegram проекты",
                    callback_data="online_tg"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_earnings"
                )
            ]
        ]
    )


def business_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💰 Идеи бизнеса",
                    callback_data="business_ideas"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📦 Продажи",
                    callback_data="business_sales"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_earnings"
                )
            ]
        ]
    )


def invest_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📚 Основы",
                    callback_data="invest_basics"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚠️ Риски",
                    callback_data="invest_risks"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_earnings"
                )
            ]
        ]
    )