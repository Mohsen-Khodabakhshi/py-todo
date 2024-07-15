from fastapi import HTTPException, Depends, status

from apps.auth.models import User
from common.jwt import jwt_handler


async def validate_user(username: str = Depends(jwt_handler.auth_wrapper)) -> User:
    user = await User.get_or_none(username=username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return user
