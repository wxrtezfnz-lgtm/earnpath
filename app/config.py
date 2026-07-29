from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    # Telegram
    BOT_TOKEN: str

    # Admin
    ADMIN_IDS: str = ""

    # Environment
    DEBUG: bool = False
    ENVIRONMENT: str = "PRODUCTION"


    # PostgreSQL
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "profitos"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = ""


    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


    # Security
    SECRET_KEY: str = "change_me"


    # Payments (если используешь)
    PAYMENT_PROVIDER_TOKEN: str = ""


    # Railway автоматически подхватывает Variables
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


    @property
    def admin_list(self):
        if not self.ADMIN_IDS:
            return []

        return [
            int(x.strip())
            for x in self.ADMIN_IDS.split(",")
            if x.strip().isdigit()
        ]


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()


# Для старого кода
BOT_TOKEN = settings.BOT_TOKEN

ADMIN_IDS = settings.admin_list

DEBUG = settings.DEBUG

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)


REDIS_URL = (
    f"redis://"
    f"{settings.REDIS_HOST}:"
    f"{settings.REDIS_PORT}"
)