from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from core.settings import database_settings

TORTOISE_ORM = {
    "connections": {"default": f"postgres://{database_settings.username}:{database_settings.password}"
                               f"@{database_settings.host}:{database_settings.port}/{database_settings.database}"},
    "apps": {
        "models": {
            "models": ["apps", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI, generate_schemas: bool = False):
    register_tortoise(
        app=app,
        config=TORTOISE_ORM,
        generate_schemas=generate_schemas,
        add_exception_handlers=True,
    )
