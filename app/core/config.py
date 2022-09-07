from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Сервис пожертвований QRKot'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    description: str = 'Домашний проект'
    secret: str = 'extra_gin'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
