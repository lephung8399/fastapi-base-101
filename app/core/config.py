from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Sửa tên biến cho khớp với biến môi trường
    DATABASE_URL: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_HOST: str
    MYSQL_ROOT_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = {
        "env_file": ".env",
        "case_sensitive": True
    }

settings = Settings()
