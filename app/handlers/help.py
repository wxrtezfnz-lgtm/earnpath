from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        """
🆘 <b>Помощь EarnPath</b>

🚀 <b>Основные команды:</b>

/start — запуск бота
/help — эта справка

💰 <b>Заработок:</b>
/earn — идеи и способы заработка

🎓 <b>Академия:</b>
/academy — обучение и материалы

👤 <b>Профиль:</b>
/profile — твой профиль

⭐ <b>Premium:</b>
/premium — доступ к расширенным функциям

Если возникли вопросы — просто напиши сообщение боту.
        """,
        parse_mode="HTML"
    )