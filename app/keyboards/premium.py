from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def premium_menu() -> InlineKeyboardMarkup:
    """
    Меню Premium ProfitOS
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⭐ Купить Premium",
                    callback_data="buy_premium"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💳 Тарифы",
                    callback_data="plans"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎁 Промокод",
                    callback_data="promo"
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