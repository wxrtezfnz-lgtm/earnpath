from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User


async def has_premium(
    user: User
) -> bool:
    """
    Проверка Premium статуса
    """

    return user.is_premium


async def enable_premium(
    session: AsyncSession,
    user: User
) -> User:
    """
    Включение Premium
    """

    user.is_premium = True

    await session.commit()
    await session.refresh(user)

    return user