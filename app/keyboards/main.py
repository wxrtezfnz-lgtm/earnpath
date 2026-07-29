from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💰 Заработок",
                    callback_data="earn"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎓 Академия",
                    callback_data="academy"
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
            ],
        ]
    )