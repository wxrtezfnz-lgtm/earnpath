from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.text == "💰 Заработок")
async def earnings(message: Message):

    await message.answer(
        "💰 Заработок\n\n"
        "Выбери направление:\n\n"
        "🔥 Фриланс\n"
        "🎨 Дизайн\n"
        "🤖 AI\n"
        "📈 Бизнес"
    )