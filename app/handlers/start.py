from aiogram import Router
from aiogram.types import Message

from app.keyboards.main import main_keyboard


router = Router()


@router.message(commands=["start"])
async def start_handler(message: Message):

    await message.answer(
        "🚀 Добро пожаловать в EarnPath!\n\n"
        "Твой путь к заработку начинается здесь.\n\n"
        "Выбери раздел ниже 👇",
        reply_markup=main_keyboard()
    )