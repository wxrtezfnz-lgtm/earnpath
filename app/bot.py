from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import settings


# handlers
from app.handlers import (
    start,
    menu,
    profile,
    earnings,
    academy,
    premium,
)


bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)


dp = Dispatcher()


# ==========================
# Регистрация обработчиков
# ==========================

dp.include_router(start.router)
dp.include_router(menu.router)
dp.include_router(profile.router)
dp.include_router(earnings.router)
dp.include_router(academy.router)
dp.include_router(premium.router)


print("✅ Все handlers подключены")