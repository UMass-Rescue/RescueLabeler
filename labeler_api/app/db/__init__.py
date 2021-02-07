from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import logging
from app.db import base  # noqa
from app.db.base_class import Base
import app.core.config as config

logger = logging.getLogger("rescue-labeler")

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    """Initialize tables with base metadata"""
    if not database_exists(engine.url):
        create_database(engine.url)
        logger.info("Created db")
        Base.metadata.create_all(bind=engine)
        logger.info("initialized_tables")


class DBContextManager:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()
