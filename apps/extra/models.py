from tortoise.models import Model
from tortoise import fields


class Test(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    age = fields.IntField()
