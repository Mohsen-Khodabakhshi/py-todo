from pydantic import BaseModel

from fastapi import status
from fastapi.responses import JSONResponse

from typing import Any


class ResponseStructure(BaseModel):
    details: Any
    status_code: int


class Response(JSONResponse):
    def __init__(self, content: Any, status_code: int = status.HTTP_200_OK, *args, **kwargs) -> None:
        content = ResponseStructure(details=content, status_code=status_code).model_dump()
        super().__init__(content, status_code, *args, **kwargs)


class Message(BaseModel):
    message: str


class Ok(BaseModel):
    details: Message = Message(message="Ok.")
    status_code: int = status.HTTP_200_OK


class Created(BaseModel):
    details: Message = Message(message="Created successfully.")
    status_code: int = status.HTTP_201_CREATED


class BadRequest(BaseModel):
    details: Message = Message(message="Bad Request.")
    status_code: int = status.HTTP_400_BAD_REQUEST


class Found(BaseModel):
    details: Message = Message(message="Found.")
    status_code: int = status.HTTP_302_FOUND


class NotFound(BaseModel):
    details: Message = Message(message="Not found.")
    status_code: int = status.HTTP_404_NOT_FOUND


class Conflict(BaseModel):
    details: Message = Message(message="Conflict.")
    status_code: int = status.HTTP_409_CONFLICT


class Forbidden(BaseModel):
    details: Message = Message(message="Forbidden.")
    status_code: int = status.HTTP_403_FORBIDDEN


class Unauthorized(BaseModel):
    details: Message = Message(message="Unauthorized.")
    status_code: int = status.HTTP_401_UNAUTHORIZED
