from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.courses import design_lessons_keyboard


router = Router()


@router.message(F.text == "🎨 Дизайн")
async def design_menu(message: Message):

    await message.answer(
        "🎨 Дизайн\n\n"
        "Выбери раздел:",
        reply_markup=design_lessons_keyboard()
    )