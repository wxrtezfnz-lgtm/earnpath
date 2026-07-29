from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repository import get_or_create_user


async def complete_lesson_progress(
    session: AsyncSession,
    telegram_id: int,
    username: str | None,
    first_name: str | None
):

    user = await get_or_create_user(
        session=session,
        telegram_id=telegram_id,
        username=username,
        first_name=first_name
    )


    user.progress += 10


    # каждые 100 очков новый уровень
    user.level = (
        user.progress // 100
    ) + 1


    await session.commit()

    await session.refresh(user)


    return user

async def add_progress(
    session: AsyncSession,
    telegram_id: int,
    amount: int = 10
):

    user = await get_user(
        session=session,
        telegram_id=telegram_id
    )


    if not user:
        return None


    user.progress += amount

    user.level = (
        user.progress // 100
    ) + 1


    await session.commit()

    await session.refresh(user)


    return user