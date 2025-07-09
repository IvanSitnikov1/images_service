from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    STATIC_PATH: str = '/home/ivan/Projects/test_tasks/images_service/static'
    class Config:
        env_file = ".env"


settings = Settings()
