from fastapi import HTTPException, status

from apps.todo.models import Project


class ToDoCRUD:
    @staticmethod
    async def get_project_by_id(project_id: int) -> Project:
        project = await Project.get_or_none(id=project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return project


todo_crud = ToDoCRUD()
