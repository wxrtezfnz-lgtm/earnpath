from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def earnings_menu() -> InlineKeyboardMarkup:
    """
    Меню направлений заработка
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🤖 AI и автоматизация",
                    callback_data="earn_ai"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💻 Фриланс",
                    callback_data="earn_freelance"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📱 Создание контента",
                    callback_data="earn_content"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏪 Онлайн-бизнес",
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
                    text="⬅ Назад",
                    callback_data="back_main"
                )
            ]
        ]
    )

    return keyboard