from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.keyboards.main import main_menu_keyboard


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "🚀 Добро пожаловать в EarnPath!\n\n"
        "Твой путь к заработку начинается здесь.\n\n"
        "Выбери раздел ниже 👇",
        reply_markup=main_menu_keyboard()
    )


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "🆘 Помощь EarnPath\n\n"
        "🚀 Основные команды:\n\n"
        "/start — запуск бота\n"
        "/help — эта справка\n\n"
        "💰 Заработок:\n"
        "/earn — идеи и способы заработка\n\n"
        "🎓 Академия:\n"
        "/academy — обучение и материалы\n\n"
        "👤 Профиль:\n"
        "/profile — твой профиль\n\n"
        "⭐ Premium:\n"
        "/premium — доступ к расширенным функциям\n\n"
        "Если возникли вопросы — просто напиши сообщение боту."
    )