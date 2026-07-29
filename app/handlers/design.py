from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.design import design_keyboard


router = Router()


@router.message(F.text == "🎨 Дизайн")
async def design_start(message: Message):
    await message.answer(
        "🎨 Дизайн\n\n"
        "Выбери раздел:",
        reply_markup=design_keyboard()
    )


@router.message(F.text == "📚 Уроки дизайна")
async def design_lessons(message: Message):
    await message.answer(
        "📚 Уроки дизайна\n\n"
        "Выбери урок:",
        reply_markup=design_lessons_keyboard()
    )


@router.message(F.text == "Урок 1 — Композиция")
async def lesson_one(message: Message):
    await message.answer(
        "🎨 Урок 1\n\n"
        "Основы композиции:\n\n"
        "• Баланс элементов\n"
        "• Контраст\n"
        "• Иерархия\n"
        "• Сетка и выравнивание\n\n"
        "Практика:\n"
        "Создай простой баннер из 3 элементов."
    )


@router.message(F.text == "Урок 2 — Цвет")
async def lesson_two(message: Message):
    await message.answer(
        "🌈 Урок 2\n\n"
        "Работа с цветом:\n\n"
        "• Цветовые схемы\n"
        "• Контраст\n"
        "• Психология цвета\n\n"
        "Практика:\n"
        "Собери палитру для проекта."
    )


@router.message(F.text == "Урок 3 — Портфолио")
async def lesson_three(message: Message):
    await message.answer(
        "🖼 Урок 3\n\n"
        "Создание портфолио:\n\n"
        "• Кейсы\n"
        "• Описание работы\n"
        "• Презентация результата\n\n"
        "Цель: сделать первый продающий кейс."
    )


def design_lessons_keyboard():
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Урок 1 — Композиция")
            ],
            [
                KeyboardButton(text="Урок 2 — Цвет")
            ],
            [
                KeyboardButton(text="Урок 3 — Портфолио")
            ],
            [
                KeyboardButton(text="🎨 Дизайн")
            ]
        ],
        resize_keyboard=True
    )