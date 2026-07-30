from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.academy import academy_keyboard


router = Router()



@router.message(F.text == "🎓 Академия")
async def academy(message: Message):

    await message.answer(
        "🎓 Академия\n\n"
        "Выбери направление:",
        reply_markup=academy_keyboard()
    )