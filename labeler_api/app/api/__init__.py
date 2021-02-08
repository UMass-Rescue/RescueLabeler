from fastapi import APIRouter
from app.api import administration, configuration, labeling
import logging

logger = logging.getLogger("rescue-labeler")


router = APIRouter()  # Primary router

router.include_router(
    administration.router, tags=["administration"], prefix="/administration"
)
router.include_router(
    configuration.router, tags=["configuration"], prefix="/configuration"
)
router.include_router(labeling.router, tags=["labeling"], prefix="/labeling")


@router.get("/")
async def home():
    """Default home route"""
    return {"msg": "RescueLab Labeler"}
