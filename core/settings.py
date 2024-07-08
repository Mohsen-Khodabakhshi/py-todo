from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class DatabaseSettings(BaseSettings):
    username: str = 'postgres'
    password: str = 'postgres'
    database: str = 'todo'
    host: str = 'localhost'
    port: int = 5432

    class Config:
        env_prefix = "DB_"


database_settings = DatabaseSettings()
