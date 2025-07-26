from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    STATIC_PATH: str = '/home/ivan/projects/test_tasks/images_service/static'
    SECRET_KEY: str
    ALGORITHM: str
    class Config:
        env_file = ".env"


settings = Settings()
