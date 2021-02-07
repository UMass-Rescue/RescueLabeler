from fastapi import FastAPI
from app.api import router as api_router
from app.core import config
from app.db import init_db
from app.core.events import create_stop_app_handler
from app import setup_logging

logger = setup_logging("rescue-labeler")


# Initalize Database
init_db()


def get_application() -> FastAPI:
    """FastAPI app generator with config parameters

    :return: FastAPI object
    :rtype: FastAPI

    """
    application = FastAPI(
        title=config.PROJECT_NAME, debug=config.DEBUG, version=config.VERSION
    )

    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.include_router(api_router, prefix=config.API_PREFIX)

    logger.info("Application ready")
    return application


app = get_application()
