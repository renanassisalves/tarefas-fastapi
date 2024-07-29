from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

#Configurações da API
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:12345@localhost:5433/tarefas'
    DBBaseModel: object = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()

