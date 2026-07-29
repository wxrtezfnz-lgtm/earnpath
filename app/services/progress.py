from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repository import (
    get_user,
    create_user as repository_create_user,
    get_or_create_user,
)



async def create_user(
    session: AsyncSession,
    telegram_id: int,
    username: str | None = None,
    first_name: str | None = None
):

    user = await get_user(
        session=session,
        telegram_id=telegram_id
    )


    if user:
        return user


    return await repository_create_user(
        session=session,
        telegram_id=telegram_id,
        username=username,
        first_name=first_name
    )



async def get_profile(
    session: AsyncSession,
    telegram_id: int
):

    return await get_user(
        session=session,
        telegram_id=telegram_id
    )



async def complete_lesson_progress(
    session: AsyncSession,
    telegram_id: int,
    username: str | None = None,
    first_name: str | None = None
):

    user = await get_or_create_user(
        session=session,
        telegram_id=telegram_id,
        username=username,
        first_name=first_name
    )


    user.progress += 10


    user.level = (
        user.progress // 100
    ) + 1


    await session.commit()
    await session.refresh(user)


    return user



async def complete_lesson(
    session: AsyncSession,
    telegram_id: int,
    username: str | None = None,
    first_name: str | None = None
):

    return await complete_lesson_progress(
        session=session,
        telegram_id=telegram_id,
        username=username,
        first_name=first_name
    )