from fastapi import FastAPI
from labeler_api.api import router as api_router
import labeler_api.core.config as config


def get_application() -> FastAPI:
    application = FastAPI(
        title=config.PROJECT_NAME, debug=config.DEBUG, version=config.VERSION
    )

    application.include_router(api_router, prefix=config.API_PREFIX)

    return application


app = get_application()
