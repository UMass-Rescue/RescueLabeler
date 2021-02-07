from fastapi import FastAPI
from labeler_api.api import router as api_router
from labeler_api.core import config


def get_application() -> FastAPI:
    """FastAPI app generator with config parameters

    :return: FastAPI object
    :rtype: FastAPI

    """
    application = FastAPI(
        title=config.PROJECT_NAME, debug=config.DEBUG, version=config.VERSION
    )

    application.include_router(api_router, prefix=config.API_PREFIX)

    return application


app = get_application()
