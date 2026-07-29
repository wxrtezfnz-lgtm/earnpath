from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def design_lessons_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📚 Уроки дизайна",
                    callback_data="design_lessons"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💼 Где искать клиентов",
                    callback_data="design_clients"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💰 Заработок дизайнера",
                    callback_data="design_money"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔙 Назад",
                    callback_data="earn"
                )
            ]
        ]
    )


def freelance_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎨 Дизайн",
                    callback_data="design"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✍️ Копирайтинг",
                    callback_data="copywriting"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💻 Программирование",
                    callback_data="programming"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🤖 AI-услуги",
                    callback_data="ai_services"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔙 Назад",
                    callback_data="earn"
                )
            ]
        ]
    )