from aiogram import Bot, Dispatcher

from app.config import BOT_TOKEN

from app.handlers import (
    start,
    menu,
    academy,
    design,
    design_progress,
    earnings,
    profile
)



bot = Bot(
    token=BOT_TOKEN
)


dp = Dispatcher()



dp.include_router(
    start.router
)

dp.include_router(
    menu.router
)

dp.include_router(
    academy.router
)

dp.include_router(
    design.router
)

dp.include_router(
    design_progress.router
)

dp.include_router(
    earnings.router
)

dp.include_router(
    profile.router
)