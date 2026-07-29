from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Основные настройки ProfitOS
    """

    # Telegram
    BOT_TOKEN: str

    # Admin
    ADMIN_IDS: str

    # Database
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str | None = None

    # Security
    SECRET_KEY: str

    # Environment
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

    @property
    def database_url(self) -> str:
        """
        URL подключения PostgreSQL
        """
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:"
            f"{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:"
            f"{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )

    @property
    def redis_url(self) -> str:
        """
        URL подключения Redis
        """

        if self.REDIS_PASSWORD:
            return (
                f"redis://:"
                f"{self.REDIS_PASSWORD}@"
                f"{self.REDIS_HOST}:"
                f"{self.REDIS_PORT}"
            )

        return (
            f"redis://"
            f"{self.REDIS_HOST}:"
            f"{self.REDIS_PORT}"
        )

    @property
    def admin_list(self) -> list[int]:
        """
        Преобразование ADMIN_IDS:
        123,456,789 -> [123,456,789]
        """

        return [
            int(admin_id.strip())
            for admin_id in self.ADMIN_IDS.split(",")
            if admin_id.strip()
        ]


@lru_cache
def get_settings() -> Settings:
    """
    Кэшируем настройки,
    чтобы не создавать объект постоянно
    """
    return Settings()


settings = get_settings()