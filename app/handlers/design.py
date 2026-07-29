from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router()


def lessons_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🎨 Урок 1 — Композиция")
            ],
            [
                KeyboardButton(text="🌈 Урок 2 — Цвет")
            ],
            [
                KeyboardButton(text="🖼 Урок 3 — Портфолио")
            ],
            [
                KeyboardButton(text="🎨 Дизайн")
            ]
        ],
        resize_keyboard=True
    )


@router.message(F.text == "🎨 Дизайн")
async def design(message: Message):
    await message.answer(
        "🎨 Дизайн\n\n"
        "Выбери раздел:",
        reply_markup=lessons_keyboard()
    )


@router.message(F.text == "📚 Уроки дизайна")
async def lessons(message: Message):
    await message.answer(
        "📚 Уроки дизайна\n\n"
        "Выбери урок:",
        reply_markup=lessons_keyboard()
    )


@router.message(F.text == "🎨 Урок 1 — Композиция")
async def lesson1(message: Message):
    await message.answer(
        "🎨 Урок 1 — Основы композиции\n\n"
        "Изучаем:\n"
        "• Баланс\n"
        "• Контраст\n"
        "• Акценты\n"
        "• Сетка\n\n"
        "Практика: сделай первый баннер."
    )


@router.message(F.text == "🌈 Урок 2 — Цвет")
async def lesson2(message: Message):
    await message.answer(
        "🌈 Урок 2 — Работа с цветом\n\n"
        "Изучаем:\n"
        "• Палитры\n"
        "• Сочетание цветов\n"
        "• Психология цвета"
    )


@router.message(F.text == "🖼 Урок 3 — Портфолио")
async def lesson3(message: Message):
    await message.answer(
        "🖼 Урок 3 — Создание портфолио\n\n"
        "Изучаем:\n"
        "• Кейсы\n"
        "• Описание проектов\n"
        "• Поиск клиентов"
    )