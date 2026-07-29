import asyncio

from loguru import logger

from app.bot import bot, dp
from app.config import settings


async def main():

    logger.info("🚀 ProfitOS запускается...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")

    try:
        # Проверка Telegram соединения
        me = await bot.get_me()

        logger.info(
            f"✅ Telegram подключен: @{me.username} "
            f"(ID: {me.id})"
        )


        # DEBUG всех входящих сообщений
        @dp.message()
        async def debug_all_messages(message):

            logger.info(
                f"📩 Получено сообщение: {message.text}"
            )

            await message.answer(
                f"✅ Получил: {message.text}"
            )


        logger.info(
            "🤖 Бот начинает polling..."
        )


        await dp.start_polling(
            bot,
            allowed_updates=[
                "message",
                "callback_query"
            ]
        )


    except Exception as e:

        logger.exception(
            f"❌ Ошибка запуска бота: {e}"
        )


    finally:

        logger.info(
            "🛑 ProfitOS остановлен"
        )

        await bot.session.close()



if __name__ == "__main__":
    asyncio.run(main())