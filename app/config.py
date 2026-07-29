from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Telegram
    BOT_TOKEN: str

    # App
    ENVIRONMENT: str = "PRODUCTION"
    DEBUG: bool = False

    # Admin
    ADMIN_IDS: str = ""

    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "profitos"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = ""

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # Security
    SECRET_KEY: str = "secret"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}"
            f"/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

BOT_TOKEN = settings.BOT_TOKEN