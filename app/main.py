import asyncio

from loguru import logger

from app.bot import bot, dp
from app.database.init_db import init_database


async def main():

    logger.info(
        "🚀 ProfitOS запускается"
    )

    await init_database()

    logger.info(
        "✅ База данных готова"
    )

    await dp.start_polling(
        bot
    )


if __name__ == "__main__":

    asyncio.run(main())