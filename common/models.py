from tortoise.models import Model
from tortoise import fields

import random


class BaseModel(Model):
    id = fields.IntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    is_active = fields.BooleanField(default=True)

    async def unique_string_value_generator(self, field_name: str, value: str) -> str:
        generator = lambda v: v + str(random.randint(1, 9))
        while await self.get_or_none(**{field_name: value}):
            value = generator(value)
        return value

    class Meta:
        abstract = True
