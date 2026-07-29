from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.engine import async_session
from app.database.repository import get_or_create_user
from app.keyboards.main import main_menu


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    """
    Регистрация пользователя и приветствие
    """

    telegram_user = message.from_user

    async with async_session() as session:

        user = await get_or_create_user(
            session=session,
            telegram_id=telegram_user.id,
            username=telegram_user.username,
            first_name=telegram_user.first_name
        )


    await message.answer(
        f"""
🚀 <b>Добро пожаловать в ProfitOS</b>

Привет, {user.first_name}! 👋

Ты зарегистрирован в системе.

Твой профиль:

🆔 ID: <code>{user.telegram_id}</code>
⭐ Статус: {"Premium" if user.is_premium else "Free"}
🎯 Уровень: {user.level}
📈 Прогресс: {user.progress}%

ProfitOS поможет тебе построить путь к доходу.

Выбери раздел 👇
        """,
        reply_markup=main_menu()
    )