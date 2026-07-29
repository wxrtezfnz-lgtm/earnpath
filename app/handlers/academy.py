from aiogram import Router
from aiogram.types import CallbackQuery

from app.keyboards.academy import academy_menu


router = Router()


@router.callback_query(
    lambda callback: callback.data == "academy"
)
async def academy_handler(
    callback: CallbackQuery
):
    """
    Главное меню Академии
    """

    await callback.message.edit_text(
        """
📚 <b>Академия ProfitOS</b>

Система обучения для роста дохода.

Выбери направление:

🎯 Старт с нуля
🤖 AI навыки
💼 Бизнес
💻 Профессии будущего

Каждый курс содержит:
✅ уроки
✅ задания
✅ прогресс
✅ практику
        """,
        reply_markup=academy_menu()
    )

    await callback.answer()