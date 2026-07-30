from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.text == "👤 Профиль")
async def profile(message: Message):

    await message.answer(
        "👤 Профиль\n\n"
        f"Имя: {message.from_user.first_name}\n"
        f"ID: {message.from_user.id}\n\n"
        "⭐ Уровень: 1\n"
        "⚡ XP: 0\n"
        "🎨 Дизайн: 0 уроков"
    )