from fastapi import HTTPException, status

from common.jwt import jwt_handler
from common.cryptography import cryptography
from apps.auth.schemas import UserRegisterIn, UserLoginIn, UserLoginOut
from apps.auth.models import User


class AuthController:
    @staticmethod
    async def register(data: UserRegisterIn) -> User:
        user = await User.get_or_none(username=data.username)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="username already exists."
            )
        user = await User.get_or_none(email=data.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="email already exists."
            )
        data.password = await cryptography.encrypt(data.password)
        user = await User.create(
            **data.dict(),
        )
        return user

    @staticmethod
    async def login(data: UserLoginIn) -> UserLoginOut:
        user = await User.get_or_none(username=data.username)
        if not user or data.password != await cryptography.decrypt(user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="username or password is wrong."
            )
        return UserLoginOut(
            access_token=await jwt_handler.encode_user(username=data.username)
        )

    @staticmethod
    async def profile(user: User) -> User:
        return user


auth_controller = AuthController()
