from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.courses_new import (
    design_lessons_keyboard,
    finish_lesson_keyboard
)


router = Router()


@router.message(F.text == "📚 Уроки дизайна")
async def lessons(message: Message):

    await message.answer(
        "🎨 Академия дизайна\n\n"
        "Выбери урок:",
        reply_markup=design_lessons_keyboard()
    )


@router.message(F.text == "🎨 Урок 1")
async def lesson_one(message: Message):

    await message.answer(
        "🎨 Урок 1 — Основы композиции\n\n"
        "Композиция — это расположение элементов.\n\n"
        "Изучаем:\n"
        "• Баланс\n"
        "• Контраст\n"
        "• Акценты\n"
        "• Сетка\n\n"
        "📝 Практика:\n"
        "Создай баннер для AI-проекта.",
        reply_markup=finish_lesson_keyboard()
    )


@router.message(F.text == "🎨 Урок 2")
async def lesson_two(message: Message):

    await message.answer(
        "🌈 Урок 2 — Работа с цветом\n\n"
        "Изучаем:\n"
        "• Палитры\n"
        "• Контраст\n"
        "• Психология цвета",
        reply_markup=finish_lesson_keyboard()
    )


@router.message(F.text == "🎨 Урок 3")
async def lesson_three(message: Message):

    await message.answer(
        "🖼 Урок 3 — Портфолио\n\n"
        "Изучаем:\n"
        "• Кейсы\n"
        "• Описание проектов\n"
        "• Поиск клиентов",
        reply_markup=finish_lesson_keyboard()
    )