from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.design import lesson_keyboard


router = Router()



@router.message(F.text == "🎨 Урок 1")
async def lesson1(message: Message):

    await message.answer(
        "🎨 Урок 1 — Основы композиции\n\n"

        "Композиция — это расположение элементов "
        "так, чтобы дизайн был понятным.\n\n"

        "Изучаем:\n"
        "• Баланс\n"
        "• Контраст\n"
        "• Акценты\n"
        "• Сетка\n\n"

        "📝 Практика:\n"
        "Создай баннер для AI-проекта.",
        
        reply_markup=lesson_keyboard()
    )