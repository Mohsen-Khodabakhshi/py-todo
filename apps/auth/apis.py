from fastapi import APIRouter, Depends, status

from apps.auth.controllers import auth_controller
from apps.auth.schemas import UserRegisterIn, UserRegisterOut, UserLoginIn, UserLoginOut, UserProfileOut
from apps.auth.dependencies import validate_user

auth_router = APIRouter(
    tags=['Authentication'],
    prefix="/auth",
)


@auth_router.post(
    "/register",
    response_model=UserRegisterOut,
    status_code=status.HTTP_201_CREATED,
)
async def register(data: UserRegisterIn):
    return await auth_controller.register(data=data)


@auth_router.post(
    "/login",
    response_model=UserLoginOut,
    status_code=status.HTTP_200_OK,
)
async def login(data: UserLoginIn):
    return await auth_controller.login(data=data)


@auth_router.get(
    "/profile",
    response_model=UserProfileOut,
    status_code=status.HTTP_200_OK,
)
async def profile(user=Depends(validate_user)):
    return await auth_controller.profile(user=user)
