from aiogram import Router
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(
    lambda callback: callback.data.startswith("earn_")
)
async def earnings_category_handler(
    callback: CallbackQuery
):
    """
    Категории заработка
    """

    category = callback.data


    if category == "earn_ai":

        text = """
🤖 <b>AI и автоматизация</b>

Направление с высоким потенциалом.

Что можно делать:

🔥 Создание AI-ботов
🔥 Автоматизация бизнеса
🔥 AI-контент
🔥 Генерация изображений
🔥 Консалтинг по внедрению AI

Первый путь:

1. Изучить инструменты AI
2. Создать 3-5 примеров работ
3. Найти первых клиентов
4. Масштабировать услуги
"""


    elif category == "earn_freelance":

        text = """
💻 <b>Фриланс</b>

Заработок через навыки.

Популярные направления:

🎨 Дизайн
✍ Копирайтинг
💻 Разработка
📊 Аналитика
🎬 Монтаж видео

Старт:

1. Выбрать навык
2. Создать портфолио
3. Найти первые заказы
4. Повысить стоимость
"""


    elif category == "earn_content":

        text = """
📱 <b>Создание контента</b>

Монетизация внимания.

Направления:

🎥 YouTube
📸 TikTok
📢 Telegram
📝 Блоги

Доход:

- реклама
- партнерки
- свои продукты
"""


    elif category == "earn_business":

        text = """
🏪 <b>Онлайн-бизнес</b>

Создание собственного проекта.

Варианты:

🚀 SaaS
🛒 Интернет-магазины
🤝 Агентства
📦 Цифровые продукты

Главное:

Найти проблему → создать решение → продать.
"""


    elif category == "earn_invest":

        text = """
📈 <b>Инвестиции</b>

Создание капитала.

Направления:

📊 Фондовый рынок
🏦 Долгосрочные активы
🌎 Диверсификация

Важно:

Сначала создать доход,
потом инвестировать.
"""


    else:

        text = """
Раздел в разработке 🚧
"""


    await callback.message.edit_text(
        text
    )

    await callback.answer()