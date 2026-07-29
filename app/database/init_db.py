from loguru import logger

from app.database.engine import engine
from app.database.models import Base
from app.database.subscription_models import Subscription
from app.database.payment_models import Payment


async def init_database():
    """
    Создание таблиц базы данных
    """

    async with engine.begin() as connection:

        await connection.run_sync(
            Base.metadata.create_all
        )

    logger.info(
        "✅ Database initialized successfully"
    )