from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import BOT_TOKEN

# =========================
# Создаем Telegram Bot
# =========================

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)


# =========================
# Dispatcher
# =========================

dp = Dispatcher()


# =========================
# Подключение handlers
# =========================

from app.handlers.start import router as start_router
from app.handlers.menu import router as menu_router
from app.handlers.profile import router as profile_router
from app.handlers.earnings import router as earnings_router
from app.handlers.academy import router as academy_router
from app.handlers.premium import router as premium_router
from app.handlers.payment import router as payment_router


def register_handlers():

    dp.include_router(start_router)

    dp.include_router(menu_router)

    dp.include_router(profile_router)

    dp.include_router(earnings_router)

    dp.include_router(academy_router)

    dp.include_router(premium_router)

    dp.include_router(payment_router)


# регистрируем при старте
register_handlers()


print("✅ Все Telegram handlers загружены")