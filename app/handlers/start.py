from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):

    await message.answer(
        """
🚀 <b>Добро пожаловать в EarnPath!</b>

Твой путь к заработку начинается здесь.

Доступные команды:

/start — запуск
/help — помощь
        """
    )