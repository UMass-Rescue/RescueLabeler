from fastapi import FastAPI
from api import router as api_router
import core.config as config


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
