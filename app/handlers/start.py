from aiogram import Router
from aiogram.types import Message

from app.keyboards.main import main_keyboard
from app.services.user_service import register_user


router = Router()



@router.message()
async def start_handler(message: Message):

    if message.text != "/start":
        return


    await register_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name
    )


    await message.answer(
        "🚀 Добро пожаловать в EarnPath!\n\n"
        "Твой путь к заработку начинается здесь.\n\n"
        "Выбери раздел 👇",
        reply_markup=main_keyboard()
    )