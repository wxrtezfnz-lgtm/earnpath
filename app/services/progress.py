from app.database.engine import async_session

from app.database.repository import (
    get_user,
    complete_design_lesson
)



async def finish_design_lesson(
    telegram_id: int
):

    async with async_session() as session:

        user = await get_user(
            session,
            telegram_id
        )


        if not user:
            return None


        user = await complete_design_lesson(
            session,
            user
        )


        return user



async def get_profile(
    telegram_id: int
):

    async with async_session() as session:

        user = await get_user(
            session,
            telegram_id
        )

        return user