from aiogram import Router
from aiogram.types import Message

from app.keyboards.earnings import earnings_keyboard


router = Router()


@router.message(lambda message: message.text == "💰 Заработок")
async def earnings_handler(message: Message):

    await message.answer(
        "💰 Заработок\n\n"
        "Выбери направление:",
        reply_markup=earnings_keyboard()
    )


@router.message(lambda message: message.text == "🔥 Фриланс")
async def freelance_handler(message: Message):

    await message.answer(
        "🔥 Фриланс\n\n"
        "Способы заработка:\n\n"
        "• Копирайтинг\n"
        "• Дизайн\n"
        "• Программирование\n"
        "• AI-услуги"
    )


@router.message(lambda message: message.text == "📱 Онлайн-проекты")
async def online_handler(message: Message):

    await message.answer(
        "📱 Онлайн-проекты\n\n"
        "• Telegram-проекты\n"
        "• Создание контента\n"
        "• Цифровые продукты"
    )


@router.message(lambda message: message.text == "🛒 Бизнес")
async def business_handler(message: Message):

    await message.answer(
        "🛒 Бизнес\n\n"
        "• Продажи\n"
        "• E-commerce\n"
        "• Услуги"
    )


@router.message(lambda message: message.text == "📈 Инвестиции")
async def investment_handler(message: Message):

    await message.answer(
        "📈 Инвестиции\n\n"
        "Обучающие материалы скоро будут доступны."
    )