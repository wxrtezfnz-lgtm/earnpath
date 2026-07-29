from aiogram import Bot, Dispatcher

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import BOT_TOKEN

from app.handlers import (
    start,
    earnings,
    design,
    help,
    profile,
    premium,
)


bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)


dp = Dispatcher()


# порядок важен
dp.include_router(start.router)
dp.include_router(earnings.router)
dp.include_router(design.router)
dp.include_router(help.router)
dp.include_router(profile.router)
dp.include_router(premium.router)