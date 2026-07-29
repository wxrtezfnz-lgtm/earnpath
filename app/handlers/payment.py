from aiogram import Router
from aiogram.types import CallbackQuery

from app.database.engine import async_session
from app.database.repository import get_user
from app.services.payment_service import create_payment


router = Router()


@router.callback_query(
    lambda callback: callback.data == "buy_premium"
)
async def buy_premium_handler(
    callback: CallbackQuery
):
    """
    Создание заказа Premium
    """

    telegram_id = callback.from_user.id


    async with async_session() as session:

        user = await get_user(
            session=session,
            telegram_id=telegram_id
        )


        if not user:

            await callback.message.answer(
                "Сначала нажми /start"
            )

            await callback.answer()

            return


        payment = await create_payment(
            session=session,
            user=user,
            amount=990
        )


    await callback.message.edit_text(
        f"""
⭐ <b>ProfitOS Premium</b>


Счет создан ✅


💳 Тариф:
Premium 30 дней


💰 Стоимость:
990 RUB


🧾 Номер заказа:
<code>{payment.id}</code>


После подключения платежной системы здесь появится кнопка оплаты.
        """
    )


    await callback.answer()