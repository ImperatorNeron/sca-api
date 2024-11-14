from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.api.routers import router as api_router


def create_app() -> FastAPI:
    application = FastAPI(
        title="SpyCatsAPI",
        docs_url="/api/docs",
        default_response_class=ORJSONResponse,
        debug=True,
    )
    application.include_router(router=api_router)
    return application
