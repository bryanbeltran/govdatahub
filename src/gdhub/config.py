from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_DSN: str = "postgresql+asyncpg://localhost/govdatahub_local"
    LOG_LEVEL: str = "INFO"


settings = Settings()
