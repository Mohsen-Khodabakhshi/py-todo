from fastapi import FastAPI, APIRouter

from apps.extra.apis import extra_router
from common import responses

main_router = APIRouter(
    responses={
        200: {"model": responses.OkResponseSchema},
        201: {"model": responses.CreatedResponseSchema},
        302: {"model": responses.FoundResponseSchema},
        400: {"model": responses.BadRequestResponseSchema},
        401: {"model": responses.UnauthorizedResponseSchema},
        403: {"model": responses.ForbiddenResponseSchema},
        404: {"model": responses.NotFoundResponseSchema},
        409: {"model": responses.ConflictResponseSchema},
    }
)


def initialize_routes(app: FastAPI):
    main_router.include_router(extra_router)

    app.include_router(main_router)
