from fastapi import APIRouter
from app.schemas.ping import PingResponseSchema
from app.api.v1.spy_cats import router as spy_cats_router
from app.api.v1.missions import router as missions_router
from app.api.v1.targets import router as targets_router

router = APIRouter(prefix="/api")

router.include_router(router=spy_cats_router)
router.include_router(router=missions_router)
router.include_router(router=targets_router)


@router.get(
    "/ping",
    response_model=PingResponseSchema,
    tags=["Ping"],
)
async def ping():
    return PingResponseSchema(result=True)
