from aiogram import Router
from aiogram.types import CallbackQuery

from app.database.engine import async_session
from app.database.repository import get_user
from app.keyboards.premium import premium_menu
from app.services.premium_service import has_premium


router = Router()


@router.callback_query(
    lambda callback: callback.data == "premium"
)
async def premium_handler(
    callback: CallbackQuery
):

    telegram_id = callback.from_user.id


    async with async_session() as session:

        user = await get_user(
            session=session,
            telegram_id=telegram_id
        )


    if not user:

        await callback.message.answer(
            "Нажми /start для регистрации"
        )

        await callback.answer()

        return



    if await has_premium(user):

        text = """
⭐ <b>ProfitOS Premium активно</b>

Твой доступ:

✅ Все курсы
✅ AI Наставник
✅ Полная база заработка
✅ Эксклюзивные материалы

Продолжай развитие 🚀
"""


    else:

        text = """
⭐ <b>ProfitOS Premium</b>

Получи полный доступ:

🔥 Все направления заработка
📚 Закрытая Академия
🧠 AI Наставник
📈 Инструменты роста

Выбери вариант:
        """


    await callback.message.edit_text(
        text,
        reply_markup=premium_menu()
    )


    await callback.answer()