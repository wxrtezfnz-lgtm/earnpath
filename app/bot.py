from aiogram import Bot, Dispatcher

from app.config import BOT_TOKEN

from app.handlers import (
    start,
    earnings,
    design,
    courses,
    profile
)


bot = Bot(
    token=BOT_TOKEN
)


dp = Dispatcher()


# Регистрация роутеров

dp.include_router(
    start.router
)

dp.include_router(
    earnings.router
)

dp.include_router(
    design.router
)

dp.include_router(
    courses.router
)

dp.include_router(
    profile.router
)
dp.include_router(design_flow.router)