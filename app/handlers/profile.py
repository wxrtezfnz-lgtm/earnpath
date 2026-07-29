from aiogram import Router
from aiogram.types import CallbackQuery

from app.database.engine import async_session
from app.services.user_service import get_user_profile


router = Router()


@router.callback_query(lambda callback: callback.data == "profile")
async def profile_handler(
    callback: CallbackQuery
):
    """
    Профиль пользователя
    """

    telegram_id = callback.from_user.id


    async with async_session() as session:

        user = await get_user_profile(
            session=session,
            telegram_id=telegram_id
        )


    if not user:

        await callback.message.answer(
            "❌ Профиль не найден. Нажми /start"
        )

        await callback.answer()

        return


    status = (
        "⭐ Premium"
        if user.is_premium
        else
        "🆓 Free"
    )


    await callback.message.edit_text(
        f"""
👤 <b>Твой профиль ProfitOS</b>

Имя:
{user.first_name}

Username:
@{user.username if user.username else "нет"}

🆔 ID:
<code>{user.telegram_id}</code>

Статус:
{status}

🎯 Уровень:
{user.level}

📈 Прогресс:
{user.progress}%

📅 Регистрация:
{user.created_at.strftime("%d.%m.%Y")}
        """
    )


    await callback.answer()