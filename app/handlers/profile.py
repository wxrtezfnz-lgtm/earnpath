from aiogram import Router, F
from aiogram.types import Message

from app.services.progress import get_profile


router = Router()



@router.message(F.text == "👤 Профиль")
async def profile(message: Message):

    user = await get_profile(
        message.from_user.id
    )


    if not user:

        await message.answer(
            "Профиль ещё не создан."
        )

        return


    await message.answer(
        "👤 Профиль\n\n"

        f"⭐ Уровень: {user.level}\n"
        f"⚡ XP: {user.xp}\n\n"

        "🎨 Дизайн:\n"
        f"{user.design_progress} уроков"
    )