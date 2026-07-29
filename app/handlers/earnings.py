from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.earnings import (
    earnings_keyboard,
    freelance_keyboard,
    online_keyboard,
    business_keyboard,
    invest_keyboard,
)


router = Router()


@router.callback_query(F.data == "earn")
async def earn_handler(callback: CallbackQuery):

    await callback.message.edit_text(
        "💰 <b>Заработок EarnPath</b>\n\n"
        "Выбери направление 👇",
        reply_markup=earnings_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "earn_freelance")
async def freelance_handler(callback: CallbackQuery):

    await callback.message.edit_text(
        "🔥 <b>Фриланс</b>\n\n"
        "Выбери раздел:",
        reply_markup=freelance_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "earn_online")
async def online_handler(callback: CallbackQuery):

    await callback.message.edit_text(
        "📱 <b>Онлайн-проекты</b>\n\n"
        "Раздел в разработке 🚧",
        reply_markup=online_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "earn_business")
async def business_handler(callback: CallbackQuery):

    await callback.message.edit_text(
        "🛒 <b>Бизнес</b>\n\n"
        "Раздел в разработке 🚧",
        reply_markup=business_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "earn_invest")
async def invest_handler(callback: CallbackQuery):

    await callback.message.edit_text(
        "📈 <b>Инвестиции</b>\n\n"
        "Раздел в разработке 🚧",
        reply_markup=invest_keyboard()
    )

    await callback.answer()