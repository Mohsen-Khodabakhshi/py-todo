from fastapi import HTTPException, status

from apps.todo.schemas import CreateProjectIn, CreateSectionIn
from apps.todo.models import Project, Section, ProjectUser
from apps.todo.crud import todo_crud
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
        project.slug = await project.unique_string_value_generator(field_name='slug', value=data.title)
        await project.save()
        await ProjectUser.create(user=user, project=project)
        return project

    @staticmethod
    async def create_section(data: CreateSectionIn, user: User) -> Section:
        project = await todo_crud.get_project_by_id(project_id=data.project_id)
        if not ProjectUser.get_or_none(
                project=project,
                user=user,
                is_active=True,
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
            )
        section = Section(**data.dict(), project=project)
        section.slug = await section.unique_string_value_generator(field_name='slug', value=data.title)
        await section.save()
        return section


todo_controller = TodoController()
