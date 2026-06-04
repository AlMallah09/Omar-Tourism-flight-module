from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Omar Tourism Flight API"
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()