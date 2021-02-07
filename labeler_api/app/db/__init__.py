from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import logging
from typing import Generator
from app.db import base  # noqa
from app.db.base_class import Base
import app.core.config as config

logger = logging.getLogger("rescue-labeler")

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)
    logger.info("Created db")


def init_db() -> None:
    """Initialize tables with base metadata"""
    Base.metadata.create_all(bind=engine)
    logger.info("initialized_tables")


def get_db() -> Generator:
    """Return a session instance generator"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
