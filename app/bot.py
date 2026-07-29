from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import BOT_TOKEN

from app.handlers.start import router as start_router


bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)


dp = Dispatcher()


# подключаем стартовый обработчик
dp.include_router(start_router)