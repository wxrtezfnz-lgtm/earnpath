from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):

    print("🔥 START RECEIVED")

    await message.answer(
        "🚀 ProfitOS работает!"
    )


@router.message()
async def all_messages(message: Message):

    print(
        f"📩 MESSAGE: {message.text}"
    )

    await message.answer(
        f"Получил: {message.text}"
    )