from aiogram import Router
from aiogram.types import CallbackQuery

from app.keyboards.earnings import earnings_menu


router = Router()


@router.callback_query(lambda callback: callback.data == "earnings")
async def earnings_handler(
    callback: CallbackQuery
):
    """
    Раздел способов заработка
    """

    await callback.message.edit_text(
        """
💰 <b>Способы заработка ProfitOS</b>

Выбери направление:

Каждый раздел содержит:

✅ Что изучить
✅ Какие навыки нужны
✅ Где искать клиентов
✅ Как получить первые деньги

Выбирай путь 👇
        """,
        reply_markup=earnings_menu()
    )

    await callback.answer()