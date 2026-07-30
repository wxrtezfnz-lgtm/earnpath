from aiogram import Router, F
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

router = Router()


def lesson_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="✅ Завершить урок")
            ]
        ],
        resize_keyboard=True,
    )


def finish_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="👤 Профиль")
            ],
            [
                KeyboardButton(text="💰 Заработок")
            ]
        ],
        resize_keyboard=True,
    )


@router.message(F.text == "🌈 Урок 2")
async def lesson2(message: Message):

    await message.answer(
        "🌈 Урок 2 — Работа с цветом\n\n"
        "Цвет помогает управлять вниманием пользователя.\n\n"
        "Изучаем:\n"
        "• Цветовые палитры\n"
        "• Контраст\n"
        "• Психология цвета\n\n"
        "📝 Практика:\n"
        "Создай 3 цветовые схемы.",
        reply_markup=lesson_keyboard(),
    )


@router.message(F.text == "🖼 Урок 3")
async def lesson3(message: Message):

    await message.answer(
        "🖼 Урок 3 — Портфолио\n\n"
        "Последний урок курса.\n\n"
        "Изучаем:\n"
        "• Кейсы\n"
        "• Behance\n"
        "• Dribbble\n"
        "• Поиск клиентов\n\n"
        "📝 Практика:\n"
        "Создай первый кейс своего проекта.",
        reply_markup=lesson_keyboard(),
    )


@router.message(F.text == "🏆 Завершить курс")
async def finish_course(message: Message):

    await message.answer(
        "🎉 Поздравляем!\n\n"
        "Ты завершил курс\n"
        "«Основы дизайна».\n\n"
        "🏆 Награда:\n"
        "+100 XP\n"
        "🎨 Статус: Junior Designer\n\n"
        "Теперь можно переходить к следующему направлению.",
        reply_markup=finish_keyboard(),
    )