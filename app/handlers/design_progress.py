from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.design import (
    next_lesson_keyboard,
    lesson_keyboard
)

from app.services.progress import (
    finish_design_lesson
)


router = Router()



@router.message(F.text == "✅ Завершить урок")
async def complete(message: Message):

    await finish_design_lesson(
        message.from_user.id
    )


    await message.answer(
        "🎉 Урок завершён!\n\n"
        "+10 XP получено.\n\n"
        "Следующий урок:\n"
        "🌈 Работа с цветом",
        reply_markup=next_lesson_keyboard()
    )



@router.message(F.text == "➡️ Следующий урок")
async def next_lesson(message: Message):

    await message.answer(
        "🌈 Урок 2 — Работа с цветом\n\n"

        "Цвет помогает управлять вниманием пользователя.\n\n"

        "Изучаем:\n"
        "• Цветовые палитры\n"
        "• Контраст цветов\n"
        "• Психология цвета\n\n"

        "📝 Практика:\n"
        "Создай 3 цветовые схемы.",
        
        reply_markup=lesson_keyboard()
    )