from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def debug_handler(message: Message):

    print(
        f"📩 MESSAGE: {message.from_user.id} -> {message.text}"
    )

    await message.answer(
        f"Получил: {message.text}"
    )