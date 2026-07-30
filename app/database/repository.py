from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User



async def get_user(
    session: AsyncSession,
    telegram_id: int
):

    result = await session.execute(
        select(User).where(
            User.telegram_id == telegram_id
        )
    )

    return result.scalar_one_or_none()



async def create_user(
    session: AsyncSession,
    telegram_id: int,
    username: str | None,
    first_name: str | None
):

    user = User(
        telegram_id=telegram_id,
        username=username,
        first_name=first_name
    )


    session.add(user)

    await session.commit()

    await session.refresh(user)

    return user



async def get_or_create_user(
    session: AsyncSession,
    telegram_id: int,
    username: str | None,
    first_name: str | None
):

    user = await get_user(
        session,
        telegram_id
    )


    if user:
        return user


    return await create_user(
        session,
        telegram_id,
        username,
        first_name
    )



async def complete_design_lesson(
    session: AsyncSession,
    user: User
):

    user.design_progress += 1

    user.xp += 10


    user.level = (
        user.xp // 100
    ) + 1


    await session.commit()

    await session.refresh(user)


    return user