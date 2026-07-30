from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    BOT_TOKEN: str

    database_url: str = (
        "sqlite+aiosqlite:///profitos.db"
    )

    ENVIRONMENT: str = "production"

    DEBUG: bool = False


    class Config:
        env_file = ".env"



settings = Settings()


BOT_TOKEN = settings.BOT_TOKEN