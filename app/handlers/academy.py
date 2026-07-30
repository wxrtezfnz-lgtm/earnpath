from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.design import design_keyboard


router = Router()



@router.message(F.text == "🎨 Дизайн")
async def design(message: Message):

    await message.answer(
        "🎨 Дизайн\n\n"
        "Выбери урок:",
        reply_markup=design_keyboard()
    )