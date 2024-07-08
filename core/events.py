from fastapi import FastAPI

from core.settings import database_settings
from services.database.connection import init_db


def database_events_handler(app: FastAPI):
    init_db(
        app=app,
        db_url=f'postgres://{database_settings.username}:{database_settings.password}'
               f'@{database_settings.host}:{database_settings.port}/{database_settings.database}',
        modules=['apps'],
    )


async def startup_event_handler(app: FastAPI) -> None:
    pass


async def shutdown_event_handler(app: FastAPI) -> None:
    pass
