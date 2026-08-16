from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Omar Tourism Flight API"
    ENVIRONMENT: Literal["development", "production", "testing"] = "development"
    DEBUG: bool = True

    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    API_V1_PREFIX: str = "/api/v1"

    LOG_LEVEL: str = "INFO"

    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173"
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    ALLOWED_HOSTS: list[str] = [
    "localhost",
    "127.0.0.1"
    ]


settings = Settings()