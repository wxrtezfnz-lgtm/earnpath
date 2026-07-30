from aiogram import Router, F
from aiogram.types import Message


router = Router()



@router.message(F.text == "💰 Заработок")
async def earnings(message: Message):

    await message.answer(
        "💰 Заработок\n\n"
        "Направления:\n"
        "🔥 Фриланс\n"
        "🤖 AI\n"
        "📈 Бизнес"
    )