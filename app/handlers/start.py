from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start_command(
    message: Message
):

    await message.answer(
        """
🚀 <b>Добро пожаловать в ProfitOS!</b>

Твой личный помощник по заработку.

Выбирай направление и начинай обучение 👇
        """
    )


@router.message(Command("help"))
async def help_command(
    message: Message
):

    await message.answer(
        "ℹ️ Используй /start чтобы открыть меню"
    )