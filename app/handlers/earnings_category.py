from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.keyboards.earnings import earnings_categories_keyboard


router = Router()


@router.message(F.text == "💰 Заработок")
async def earnings_menu(message: Message):
    await message.answer(
        "💰 <b>Раздел заработка</b>\n\n"
        "Выбери направление 👇",
        reply_markup=earnings_categories_keyboard()
    )


@router.callback_query(F.data.startswith("earn_"))
async def earnings_category(callback: CallbackQuery):

    category = callback.data.replace("earn_", "")

    data = {

        "freelance":
        (
            "🔥 <b>Фриланс</b>\n\n"
            "Способ заработка через навыки.\n\n"
            "Примеры:\n"
            "• Дизайн\n"
            "• Монтаж видео\n"
            "• Копирайтинг\n"
            "• Разработка\n\n"
            "Следующий шаг — выбери навык и начни делать портфолио."
        ),

        "online":
        (
            "📱 <b>Онлайн-проекты</b>\n\n"
            "Создание дохода через интернет:\n\n"
            "• Telegram проекты\n"
            "• AI сервисы\n"
            "• Цифровые продукты\n"
            "• Автоматизация"
        ),

        "business":
        (
            "🛒 <b>Бизнес</b>\n\n"
            "Идеи малого бизнеса:\n\n"
            "• Услуги\n"
            "• Продажи\n"
            "• Агентские модели\n"
            "• Микропроекты"
        ),

        "invest":
        (
            "📈 <b>Инвестиции</b>\n\n"
            "Основы:\n\n"
            "• Акции\n"
            "• ETF\n"
            "• Долгосрочные стратегии\n"
            "• Управление рисками"
        )

    }


    await callback.message.answer(
        data.get(
            category,
            "Раздел скоро будет доступен 🚧"
        )
    )

    await callback.answer()