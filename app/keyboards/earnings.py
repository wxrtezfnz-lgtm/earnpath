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
            ],
        ]
    )


def freelance_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✍️ Копирайтинг",
                    callback_data="skill_copywriting"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎨 Дизайн",
                    callback_data="skill_design"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💻 Разработка",
                    callback_data="skill_dev"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🤖 AI-инструменты",
                    callback_data="skill_ai"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_earn"
                )
            ],
        ]
    )