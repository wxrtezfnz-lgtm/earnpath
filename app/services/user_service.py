from app.database.repository import (
    get_or_create_user
)

from app.database.engine import async_session


async def register_user(
    telegram_id: int,
    username: str | None,
    first_name: str | None
):

    async with async_session() as session:

        user = await get_or_create_user(
            session=session,
            telegram_id=telegram_id,
            username=username,
            first_name=first_name
        )

        return user