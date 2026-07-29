from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda c: c.data == "earn")
async def earn_callback(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "💰 <b>Заработок</b>\n\n"
        "Выбери направление:\n\n"
        "🔥 Фриланс\n"
        "📱 Онлайн-проекты\n"
        "🛒 Бизнес\n"
        "📈 Инвестиции\n\n"
        "Скоро добавим подробные материалы."
    )


@router.callback_query(lambda c: c.data == "academy")
async def academy_callback(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "🎓 <b>Академия EarnPath</b>\n\n"
        "Уроки и материалы скоро будут доступны."
    )


@router.callback_query(lambda c: c.data == "profile")
async def profile_callback(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "👤 <b>Профиль</b>\n\n"
        "Раздел профиля в разработке."
    )


@router.callback_query(lambda c: c.data == "premium")
async def premium_callback(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "⭐ <b>Premium EarnPath</b>\n\n"
        "Расширенные возможности скоро будут доступны."
    )