from datetime import datetime
from pydantic import BaseModel, EmailStr, field_validator
from fastapi import HTTPException, status


class PasswordModel(BaseModel):
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 8 characters long.",
            )
        return value


class UserRegisterIn(PasswordModel):
    name: str
    username: str
    email: EmailStr


class UserRegisterOut(BaseModel):
    name: str
    username: str
    email: EmailStr


class UserProfileOut(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    name: str
    avatar: str | None = None
    last_login: datetime | None = None


class UserLoginIn(BaseModel):
    username: str
    password: str


class UserLoginOut(BaseModel):
    access_token: str
