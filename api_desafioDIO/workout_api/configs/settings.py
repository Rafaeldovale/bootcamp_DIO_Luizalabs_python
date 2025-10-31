from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_UL: str = Field(default='postgresql+asyncpg://workout:workout@localhost/dbname')

settings = Settings()

