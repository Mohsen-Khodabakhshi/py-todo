from pydantic import BaseModel

from fastapi import status
from fastapi.responses import JSONResponse

from typing import Any


class ResponseStructure(BaseModel):
    details: Any
    status_code: int


class ResponseSchema(JSONResponse):
    def __init__(self, content: Any, status_code: int = status.HTTP_200_OK, *args, **kwargs) -> None:
        content = ResponseStructure(details=content, status_code=status_code).model_dump()
        super().__init__(content, status_code, *args, **kwargs)


class Message(BaseModel):
    message: str


class OkResponseSchema(BaseModel):
    details: Message = Message(message="Ok.")
    status_code: int = status.HTTP_200_OK


class CreatedResponseSchema(BaseModel):
    details: Message = Message(message="Created successfully.")
    status_code: int = status.HTTP_201_CREATED


class BadRequestResponseSchema(BaseModel):
    details: Message = Message(message="Bad Request.")
    status_code: int = status.HTTP_400_BAD_REQUEST


class FoundResponseSchema(BaseModel):
    details: Message = Message(message="Found.")
    status_code: int = status.HTTP_302_FOUND


class NotFoundResponseSchema(BaseModel):
    details: Message = Message(message="Not found.")
    status_code: int = status.HTTP_404_NOT_FOUND


class ConflictResponseSchema(BaseModel):
    details: Message = Message(message="Conflict.")
    status_code: int = status.HTTP_409_CONFLICT


class ForbiddenResponseSchema(BaseModel):
    details: Message = Message(message="Forbidden.")
    status_code: int = status.HTTP_403_FORBIDDEN


class UnauthorizedResponseSchema(BaseModel):
    details: Message = Message(message="Unauthorized.")
    status_code: int = status.HTTP_401_UNAUTHORIZED
