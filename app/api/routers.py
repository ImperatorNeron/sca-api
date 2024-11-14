from fastapi import APIRouter
from app.schemas.ping import PingResponseSchema
from app.api.v1.spy_cats import router as spy_cats_router

router = APIRouter(prefix="/api")

router.include_router(router=spy_cats_router)


@router.get(
    "/ping",
    response_model=PingResponseSchema,
    tags=["Ping"],
)
async def ping():
    return PingResponseSchema(result=True)
