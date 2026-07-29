from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(
    message: Message
):

    print(
        f"START FROM {message.from_user.id}"
    )

    await message.answer(
        """
🚀 <b>Добро пожаловать в EarnPath!</b>

Твой путь к заработку начинается здесь.

Доступные команды:

/start — запуск
/help — помощь
        """
    )


@router.message(Command("help"))
async def help_handler(
    message: Message
):

    await message.answer(
        "ℹ️ Помощь EarnPath"
    )


@router.message()
async def echo_handler(
    message: Message
):

    print(
        f"MSG: {message.text}"
    )

    await message.answer(
        f"✅ Получил: {message.text}"
    )