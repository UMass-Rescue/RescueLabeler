from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.db import DBContextManager
import logging

logger = logging.getLogger("rescue-labeler")


router = APIRouter()  # Primary router

# TODO: Remove
# router.include_router(authentication.router, tags=["authentication"], prefix="/users")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
async def home():
    """Default home route"""
    return {"msg": "RescueLab Labeler"}


@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    """TODO update"""
    return {"token": token}


@router.get("/db_test/")
async def db_test():
    with DBContextManager() as db:
        logger.info(db)
    return {"hi": "hey"}
