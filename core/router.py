from fastapi import FastAPI, APIRouter

from apps.extra.apis import extra_router
from apps.auth.apis import auth_router
from apps.todo.apis import todo_router

main_router = APIRouter()


def initialize_routes(app: FastAPI):
    main_router.include_router(extra_router)

    app.include_router(main_router)
    app.include_router(auth_router)
    app.include_router(todo_router)
