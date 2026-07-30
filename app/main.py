import asyncio

from loguru import logger

from app.bot import bot, dp



async def main():

    logger.info(
        "🚀 ProfitOS запущен"
    )


    await dp.start_polling(
        bot
    )



if __name__ == "__main__":

    asyncio.run(main())