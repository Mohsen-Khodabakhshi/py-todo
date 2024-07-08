from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


def init_db(app: FastAPI, db_url: str, modules: list, generate_schemas: bool = True):
    register_tortoise(
        app=app,
        db_url=db_url,
        modules={'models': modules},
        generate_schemas=generate_schemas,
        add_exception_handlers=True,
    )
