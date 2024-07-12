from fastapi import FastAPI

from services.database.connection import init_db


def database_events_handler(app: FastAPI):
    init_db(app=app)


async def startup_event_handler(app: FastAPI) -> None:
    pass


async def shutdown_event_handler(app: FastAPI) -> None:
    pass
