from typing import Callable

from fastapi import FastAPI
from app.core.config import DEBUG
from app.db import engine
from sqlalchemy_utils import database_exists, drop_database
import logging

logger = logging.getLogger("rescue-labeler")


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def stop_app() -> None:
        """Delete the db in debug mode"""
        if DEBUG and database_exists(engine.url):
            drop_database(engine.url)
            logger.info("db dropped")

    return stop_app
