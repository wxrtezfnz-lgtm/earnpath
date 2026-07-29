from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.design import design_keyboard


router = Router()


@router.message(F.text == "🎨 Дизайн")
async def design_start(message: Message):
    await message.answer(
        "🎨 Дизайн\n\n"
        "Выбери раздел:\n\n"
        "📚 Уроки дизайна\n"
        "💼 Поиск клиентов\n"
        "🧰 Инструменты",
        reply_markup=design_keyboard()
    )


@router.message(F.text == "📚 Уроки дизайна")
async def design_lessons(message: Message):
    await message.answer(
        "📚 Уроки дизайна\n\n"
        "Урок 1:\n"
        "🎨 Основы композиции\n\n"
        "Урок 2:\n"
        "🌈 Работа с цветом\n\n"
        "Урок 3:\n"
        "🖼 Создание портфолио\n\n"
        "Скоро добавим полноценные материалы 🚀"
    )


@router.message(F.text == "💼 Поиск клиентов")
async def design_clients(message: Message):
    await message.answer(
        "💼 Поиск клиентов\n\n"
        "Где искать заказы:\n\n"
        "• Upwork\n"
        "• Fiverr\n"
        "• Telegram-чаты\n"
        "• Социальные сети"
    )


@router.message(F.text == "🧰 Инструменты")
async def design_tools(message: Message):
    await message.answer(
        "🧰 Инструменты дизайнера:\n\n"
        "• Figma\n"
        "• Photoshop\n"
        "• Illustrator\n"
        "• Canva\n"
        "• Midjourney AI"
    )