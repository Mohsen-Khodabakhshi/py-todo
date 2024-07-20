from fastapi import APIRouter, Depends, status

from apps.todo.controllers import todo_controller
from apps.todo.schemas import CreateProjectIn, CreateProjectOut
from apps.auth.dependencies import validate_user
from apps.auth.models import User

todo_router = APIRouter(
    tags=['ToDo'],
    prefix="/todo",
)


@todo_router.post(
    "/project",
    response_model=CreateProjectOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_project(data: CreateProjectIn, user: User = Depends(validate_user)):
    return await todo_controller.create_project(data=data, user=user)
