from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router()


def after_lesson_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="➡️ Следующий урок"
                )
            ],
            [
                KeyboardButton(
                    text="🎨 Дизайн"
                )
            ]
        ],
        resize_keyboard=True
    )


@router.message(F.text == "✅ Завершить урок")
async def complete_lesson(message: Message):

    await message.answer(
        "🎉 Урок завершён!\n\n"
        "Ты получил +10 XP.\n\n"
        "Следующий шаг:\n"
        "🌈 Урок 2 — Работа с цветом",
        reply_markup=after_lesson_keyboard()
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
        "Создай 3 цветовые схемы для бренда.",
    )