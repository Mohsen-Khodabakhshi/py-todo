from fastapi import HTTPException, status

from apps.todo.schemas import CreateProjectIn
from apps.todo.models import Project
from apps.auth.models import User


class TodoController:
    @staticmethod
    async def create_project(data: CreateProjectIn, user: User) -> Project:
        if await Project.get_or_none(owner=user, title=data.title):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Project with this title is exist."
            )
        project = Project(owner=user, **data.dict())
        project.slug = await project.slug_generator()
        await project.save()
        return project


todo_controller = TodoController()
