from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.keyboards.lessons import freelance_keyboard, design_lessons_keyboard


router = Router()


@router.message(F.text == "🔥 Фриланс")
async def freelance(message: Message):
    await message.answer(
        """
🔥 Фриланс

Выбери направление:
""",
        reply_markup=freelance_keyboard()
    )


@router.callback_query(F.data == "design")
async def design(callback: CallbackQuery):
    await callback.message.edit_text(
        """
🎨 Дизайн

Направления:

• Логотипы
• Баннеры
• UI/UX

Выбери действие:
""",
        reply_markup=design_lessons_keyboard()
    )


@router.callback_query(F.data == "design_lessons")
async def design_lessons(callback: CallbackQuery):
    await callback.message.edit_text(
        """
📚 Уроки дизайна

Урок 1:
Основы композиции

Урок 2:
Работа с цветом

Урок 3:
Создание портфолио

Скоро добавим материалы 🚀
"""
    )


@router.callback_query(F.data == "design_clients")
async def design_clients(callback: CallbackQuery):
    await callback.message.edit_text(
        """
💼 Где искать клиентов

• Upwork
• Fiverr
• Telegram
• Behance

Гайд скоро будет доступен.
"""
    )


@router.callback_query(F.data == "design_money")
async def design_money(callback: CallbackQuery):
    await callback.message.edit_text(
        """
💰 Заработок дизайнера

Новичок:
$100-500 / месяц

Опытный:
$1000+

Senior:
$3000+
"""
    )