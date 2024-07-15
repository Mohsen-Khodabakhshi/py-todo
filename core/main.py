from fastapi import FastAPI

from middlewares.response_handler import response_handler_middleware
from core.router import initialize_routes
from core import events

app = FastAPI()

response_handler_middleware(app)

events.database_events_handler(app=app)


@app.on_event("startup")
async def startup() -> None:
    await events.startup_event_handler(app=app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await events.shutdown_event_handler(app=app)


initialize_routes(app)
