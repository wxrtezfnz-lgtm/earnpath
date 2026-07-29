from aiogram import Bot, Dispatcher

from app.config import BOT_TOKEN

from app.handlers import (
    start,
    earnings,
    profile,
    design_flow
)


bot = Bot(
    token=BOT_TOKEN
)


dp = Dispatcher()


# Основные роутеры

dp.include_router(
    start.router
)

dp.include_router(
    earnings.router
)

dp.include_router(
    design_flow.router
)

dp.include_router(
    profile.router
)