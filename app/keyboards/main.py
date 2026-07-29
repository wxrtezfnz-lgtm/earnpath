from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu() -> InlineKeyboardMarkup:
    """
    Главное меню ProfitOS
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💰 Способы заработка",
                    callback_data="earnings"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🧠 AI Наставник",
                    callback_data="ai_coach"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📚 Академия",
                    callback_data="academy"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📈 Инструменты",
                    callback_data="tools"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎯 План развития",
                    callback_data="roadmap"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👤 Профиль",
                    callback_data="profile"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⭐ Premium",
                    callback_data="premium"
                )
            ]
        ]
    )

    return keyboard