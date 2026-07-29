from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User
from app.database.repository import get_user


async def get_user_profile(
    session: AsyncSession,
    telegram_id: int
) -> User | None:
    """
    Получение профиля пользователя
    """

    return await get_user(
        session=session,
        telegram_id=telegram_id
    )


async def activate_premium(
    session: AsyncSession,
    user: User
) -> User:
    """
    Активация Premium подписки
    """

    user.is_premium = True

    await session.commit()
    await session.refresh(user)

    return user


async def increase_level(
    session: AsyncSession,
    user: User
) -> User:
    """
    Повышение уровня пользователя
    """

    user.level += 1

    await session.commit()
    await session.refresh(user)

    return user


async def update_progress(
    session: AsyncSession,
    user: User,
    value: int
) -> User:
    """
    Изменение прогресса обучения
    """

    user.progress += value

    if user.progress > 100:
        user.progress = 100

    await session.commit()
    await session.refresh(user)

    return user