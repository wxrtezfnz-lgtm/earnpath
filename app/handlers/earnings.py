from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.earnings import (
    earnings_keyboard,
    freelance_keyboard,
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
        "• Telegram-проекты\n"
        "• Создание контента\n"
        "• Цифровые продукты"
    )


@router.message(F.text == "🛒 Бизнес")
async def business(message: Message):
    await message.answer(
        "🛒 Бизнес\n\n"
        "• Продажи\n"
        "• E-commerce\n"
        "• Услуги"
    )


@router.message(F.text == "📈 Инвестиции")
async def investments(message: Message):
    await message.answer(
        "📈 Инвестиции\n\n"
        "Материалы скоро будут доступны 🚀"
    )