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

    user.level = (
        user.progress // 100
    ) + 1


    await session.commit()
    await session.refresh(user)


    return user



# совместимость со старыми handlers
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