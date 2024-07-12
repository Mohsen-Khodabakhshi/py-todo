from common.models import BaseModel

from tortoise import fields


class User(BaseModel):
    username = fields.CharField(max_length=64, unique=True, db_index=True)
    password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    name = fields.CharField(max_length=64, null=True)
    avatar = fields.CharField(max_length=255)
    last_login = fields.DatetimeField(null=True)

    def __str__(self) -> str:
        return f'{self.username}'
