from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.earnings import (
    earnings_keyboard,
    freelance_keyboard,
    online_projects_keyboard,
    business_keyboard,
    investments_keyboard,
)

router = Router()


@router.message(F.text == "💰 Заработок")
async def earnings(message: Message):
    await message.answer(
        "💰 Заработок\n\n"
        "Выбери направление:",
        reply_markup=earnings_keyboard()
    )


@router.message(F.text == "🔥 Фриланс")
async def freelance(message: Message):
    await message.answer(
        "🔥 Фриланс\n\n"
        "Выбери направление:",
        reply_markup=freelance_keyboard()
    )


@router.message(F.text == "📱 Онлайн-проекты")
async def online_projects(message: Message):
    await message.answer(
        "📱 Онлайн-проекты\n\n"
        "Выбери направление:",
        reply_markup=online_projects_keyboard()
    )


@router.message(F.text == "🛒 Бизнес")
async def business(message: Message):
    await message.answer(
        "🛒 Бизнес\n\n"
        "Выбери направление:",
        reply_markup=business_keyboard()
    )


@router.message(F.text == "📈 Инвестиции")
async def investments(message: Message):
    await message.answer(
        "📈 Инвестиции\n\n"
        "Обучающие материалы скоро будут доступны.",
        reply_markup=investments_keyboard()
    )


# Фриланс категории

@router.message(F.text == "💻 Копирайтинг")
async def copywriting(message: Message):
    await message.answer(
        "💻 Копирайтинг\n\n"
        "Заработок на текстах:\n\n"
        "• Статьи\n"
        "• Описания товаров\n"
        "• Посты для соцсетей"
    )


@router.message(F.text == "🎨 Дизайн")
async def design(message: Message):
    await message.answer(
        "🎨 Дизайн\n\n"
        "Направления:\n\n"
        "• Логотипы\n"
        "• Баннеры\n"
        "• UI/UX"
    )


@router.message(F.text == "👨‍💻 Программирование")
async def programming(message: Message):
    await message.answer(
        "👨‍💻 Программирование\n\n"
        "Возможности:\n\n"
        "• Сайты\n"
        "• Боты\n"
        "• Автоматизация"
    )


@router.message(F.text == "🤖 AI-услуги")
async def ai_services(message: Message):
    await message.answer(
        "🤖 AI-услуги\n\n"
        "Заработок с AI:\n\n"
        "• Создание контента\n"
        "• Автоматизация\n"
        "• AI-консалтинг"
    )


@router.message(F.text == "🔙 Назад")
async def back(message: Message):
    await message.answer(
        "Выбери раздел 👇",
        reply_markup=earnings_keyboard()
    )