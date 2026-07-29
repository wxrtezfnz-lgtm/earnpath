from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from app.config import settings


engine = create_async_engine(
    url=settings.database_url,
    echo=settings.DEBUG,
    pool_pre_ping=True
)


async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session() -> AsyncSession:
    """
    Создание сессии базы данных
    """

    async with async_session() as session:
        return session