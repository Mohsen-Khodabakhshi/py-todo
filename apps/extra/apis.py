from fastapi import APIRouter

extra_router = APIRouter(
    tags=['Extra'],
    prefix="",
)


@extra_router.get("/health")
def health_check():
    return {"message": "ok"}
