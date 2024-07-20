import random

from tortoise import fields

from common.models import BaseModel
from apps.todo.enums import TaskPriority, ProjectUserStatus


class Project(BaseModel):
    title = fields.CharField(max_length=64, unique=True)
    slug = fields.CharField(max_length=64, db_index=True)
    order = fields.SmallIntField(default=1)
    owner: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User',
        related_name='projects',
        on_delete=fields.CASCADE
    )

    async def slug_generator(self):
        slug = self.title
        generator = lambda s: s + str(random.randint(1, 9))
        while True:
            if not await Project.get_or_none(slug=slug):
                break
            slug = generator(slug)
        return slug

    def __str__(self) -> str:
        return f'{self.owner} - {self.title}'


class ProjectUser(BaseModel):
    project: fields.ForeignKeyRelation['Project'] = fields.ForeignKeyField(
        'models.Project',
        related_name='users',
        on_delete=fields.CASCADE
    )
    user = fields.ForeignKeyField('models.User', related_name='user_projects', on_delete=fields.CASCADE)
    status = fields.CharEnumField(ProjectUserStatus, default=ProjectUserStatus.INVITED.value)

    def __str__(self) -> str:
        return f'{self.project} - {self.user}'


class Section(BaseModel):
    title = fields.CharField(max_length=64)
    slug = fields.CharField(max_length=64, db_index=True)
    order = fields.SmallIntField(default=1)
    project: fields.ForeignKeyRelation['Project'] = fields.ForeignKeyField(
        'models.Project',
        related_name='sections',
        on_delete=fields.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.project} - {self.title}'


class Task(BaseModel):
    title = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    slug = fields.CharField(max_length=64, db_index=True)
    section = fields.ForeignKeyField('models.Section', related_name='tasks', on_delete=fields.CASCADE)
    assign_to: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User',
        related_name='tasks',
        on_delete=fields.CASCADE,
        null=True,
    )
    due_date = fields.DatetimeField(null=True)
    order = fields.SmallIntField(default=1)
    priority = fields.CharEnumField(TaskPriority, default=TaskPriority.PRIORITY_LOW.value)
    parent: fields.ForeignKeyRelation['Task'] = fields.ForeignKeyField(
        'models.Task',
        related_name='sub_tasks',
        on_delete=fields.CASCADE,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.section.project} - {self.title}'


class Comment(BaseModel):
    body = fields.TextField()
    user: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User',
        related_name='comments',
        on_delete=fields.CASCADE
    )
    task: fields.ForeignKeyRelation['Task'] = fields.ForeignKeyField(
        'models.Task',
        related_name='comments',
        on_delete=fields.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.task} - {self.user}'
