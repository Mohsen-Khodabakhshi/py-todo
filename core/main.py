from fastapi import FastAPI

from common.responses import ResponseSchema
from core.router import initialize_routes

app = FastAPI(default_response_class=ResponseSchema)

initialize_routes(app)
