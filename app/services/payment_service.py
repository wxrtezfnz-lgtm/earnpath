from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.payment_models import Payment
from app.database.models import User
from app.database.subscription_models import Subscription
from app.services.subscription_service import (
    create_subscription,
    activate_subscription
)


async def create_payment(
    session: AsyncSession,
    user: User,
    amount: int = 990
) -> Payment:
    """
    Создание платежа
    """

    payment = Payment(
        user_id=user.id,
        amount=amount,
        currency="RUB"
    )

    session.add(payment)

    await session.commit()
    await session.refresh(payment)

    return payment



async def get_payment(
    session: AsyncSession,
    payment_id: int
) -> Payment | None:
    """
    Получение платежа
    """

    result = await session.execute(
        select(Payment)
        .where(
            Payment.id == payment_id
        )
    )

    return result.scalar_one_or_none()



async def complete_payment(
    session: AsyncSession,
    payment: Payment,
    user: User
):
    """
    Завершение оплаты
    """

    payment.is_paid = True


    subscription = await create_subscription(
        session=session,
        user=user
    )


    await activate_subscription(
        session=session,
        subscription=subscription,
        days=30
    )


    user.is_premium = True


    await session.commit()


    return payment