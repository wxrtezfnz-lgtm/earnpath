from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from app.keyboards.main import main_keyboard
from app.keyboards.earnings import earnings_keyboard


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "🚀 Добро пожаловать в EarnPath!\n\n"
        "Твой путь к заработку начинается здесь.\n\n"
        "Выбери раздел ниже 👇",
        reply_markup=main_keyboard()
    )


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "🆘 Помощь EarnPath\n\n"
        "🚀 Основные команды:\n\n"
        "/start — запуск бота\n"
        "/help — помощь\n\n"
        "💰 Заработок:\n"
        "/earn — идеи и способы заработка\n\n"
        "🎓 Академия:\n"
        "/academy — обучение\n\n"
        "👤 Профиль:\n"
        "/profile — профиль\n\n"
        "⭐ Premium:\n"
        "/premium — возможности"
    )


@router.message(F.text == "💰 Заработок")
async def earnings_handler(message: Message):
    await message.answer(
        "💰 Заработок\n\n"
        "Выбери направление:",
        reply_markup=earnings_keyboard()
    )