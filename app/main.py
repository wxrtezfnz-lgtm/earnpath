import asyncio

from loguru import logger

from app.bot import bot, dp
from app.config import settings


async def main():
    """
    Главный запуск ProfitOS
    """

    logger.info("🚀 ProfitOS запускается...")

    logger.info(
        f"Environment: {'DEBUG' if settings.DEBUG else 'PRODUCTION'}"
    )

    try:
        await dp.start_polling(bot)

    except Exception as error:
        logger.exception(
            f"Ошибка запуска бота: {error}"
        )

    finally:
        await bot.session.close()
        logger.info("🛑 ProfitOS остановлен")


if __name__ == "__main__":
    asyncio.run(main())