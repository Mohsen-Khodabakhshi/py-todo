from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserRegisterIn(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str


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
