from aiogram import Router, F
from aiogram.types import Message

from app.services.progress import (
    get_profile,
    create_user
)


router = Router()


@router.message(F.text == "👤 Профиль")
async def profile(message: Message):

    user = get_profile(
        message.from_user.id
    )


    if not user:

        user = create_user(
            message.from_user.id,
            message.from_user.username or "user"
        )


    await message.answer(
        "👤 Твой профиль\n\n"
        f"Игрок: {user['username']}\n\n"
        f"⭐ Уровень: {user['level']}\n"
        f"⚡ XP: {user['xp']}\n\n"
        f"🎨 Дизайн:\n"
        f"{len(user['lessons'])}/10 уроков"
    )