from aiogram import Router
from aiogram.types import CallbackQuery

from app.keyboards.earnings import (
    earnings_keyboard,
    freelance_keyboard
)


router = Router()


@router.callback_query(lambda c: c.data == "earn")
async def earnings_menu(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "💰 <b>Заработок</b>\n\n"
        "Выбери направление:",
        reply_markup=earnings_keyboard()
    )


@router.callback_query(lambda c: c.data == "earn_freelance")
async def freelance_menu(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "🔥 <b>Фриланс</b>\n\n"
        "Выбери навык:",
        reply_markup=freelance_keyboard()
    )


@router.callback_query(lambda c: c.data == "earn_online")
async def online(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "📱 <b>Онлайн-проекты</b>\n\n"
        "Скоро добавим лучшие варианты."
    )


@router.callback_query(lambda c: c.data == "earn_business")
async def business(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "🛒 <b>Бизнес</b>\n\n"
        "Идеи и стратегии скоро появятся."
    )


@router.callback_query(lambda c: c.data == "earn_invest")
async def invest(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "📈 <b>Инвестиции</b>\n\n"
        "Материалы готовятся."
    )


@router.callback_query(lambda c: c.data == "skill_ai")
async def ai_skill(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "🤖 <b>AI-инструменты</b>\n\n"
        "Урок 1:\n"
        "Как использовать ИИ для заработка\n\n"
        "Урок 2:\n"
        "Автоматизация задач\n\n"
        "Урок 3:\n"
        "Поиск клиентов через AI"
    )


@router.callback_query(lambda c: c.data == "skill_copywriting")
async def copywriting(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "✍️ <b>Копирайтинг</b>\n\n"
        "Материалы скоро будут доступны."
    )


@router.callback_query(lambda c: c.data == "skill_design")
async def design(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "🎨 <b>Дизайн</b>\n\n"
        "Материалы скоро будут доступны."
    )


@router.callback_query(lambda c: c.data == "skill_dev")
async def dev(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "💻 <b>Разработка</b>\n\n"
        "Материалы скоро будут доступны."
    )


@router.callback_query(lambda c: c.data == "back_earn")
async def back_earn(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "💰 <b>Заработок</b>\n\n"
        "Выбери направление:",
        reply_markup=earnings_keyboard()
    )