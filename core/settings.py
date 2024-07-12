from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class AppSettings(BaseSettings):
    secret_key: str = 'secret_key'

    class Config:
        env_prefix = "APP_"


app_settings = AppSettings()


class DatabaseSettings(BaseSettings):
    username: str = 'postgres'
    password: str = 'postgres'
    database: str = 'todo'
    host: str = 'localhost'
    port: int = 5432

    class Config:
        env_prefix = "DB_"


database_settings = DatabaseSettings()


class JWTSettings(BaseSettings):
    algorithm: str = 'HS256'
    access_token_expire_minutes = 525600

    class Config:
        env_prefix = "JWT_"


jwt_settings = JWTSettings()
