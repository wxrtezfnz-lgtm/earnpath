from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def academy_menu() -> InlineKeyboardMarkup:
    """
    Меню Академии ProfitOS
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎯 Старт с нуля",
                    callback_data="academy_start"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🤖 AI Навыки",
                    callback_data="academy_ai"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💼 Бизнес",
                    callback_data="academy_business"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💻 Профессии будущего",
                    callback_data="academy_future"
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