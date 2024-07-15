import json

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from common.responses import ResponseStructure

specific_paths = []


def response_handler_middleware(app: FastAPI):
    @app.middleware("http")
    async def _(request: Request, call_next):
        response = await call_next(request)
        if request.url.path in [
            app.docs_url,
            app.openapi_url,
            app.redoc_url,
            app.swagger_ui_oauth2_redirect_url,
            *specific_paths,
        ]:
            return response
        response_body = [chunk async for chunk in response.body_iterator][0].decode()
        json_response_body = json.loads(response_body)
        response_structure = ResponseStructure(
            details=json_response_body,
            status_code=response.status_code,
        )
        headers = dict(response.headers)
        headers.pop('content-length', None)
        return JSONResponse(
            content=jsonable_encoder(response_structure),
            status_code=response.status_code,
            media_type=response.media_type,
            headers=headers,
        )
