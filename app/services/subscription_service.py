from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.subscription_models import Subscription
from app.database.models import User


async def get_subscription(
    session: AsyncSession,
    user_id: int
) -> Subscription | None:
    """
    Получение подписки пользователя
    """

    result = await session.execute(
        select(Subscription)
        .where(
            Subscription.user_id == user_id
        )
        .order_by(
            Subscription.id.desc()
        )
    )

    return result.scalar_one_or_none()



async def create_subscription(
    session: AsyncSession,
    user: User,
    plan: str = "premium"
) -> Subscription:
    """
    Создание новой подписки
    """

    subscription = Subscription(
        user_id=user.id,
        plan=plan,
        is_active=False
    )

    session.add(subscription)

    await session.commit()
    await session.refresh(subscription)

    return subscription



async def activate_subscription(
    session: AsyncSession,
    subscription: Subscription,
    days: int = 30
) -> Subscription:
    """
    Активация подписки
    """

    subscription.is_active = True

    subscription.expires_at = (
        datetime.utcnow()
        +
        timedelta(days=days)
    )

    await session.commit()
    await session.refresh(subscription)

    return subscription



async def check_subscription(
    subscription: Subscription
) -> bool:
    """
    Проверка активности подписки
    """

    if not subscription:
        return False


    if not subscription.is_active:
        return False


    if subscription.expires_at:

        if subscription.expires_at < datetime.utcnow():

            return False


    return True