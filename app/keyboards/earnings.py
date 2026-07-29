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
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_main"
                )
            ]
        ]
    )