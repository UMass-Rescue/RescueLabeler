from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer


router = APIRouter()  # Primary router

# TODO: Remove
# router.include_router(authentication.router, tags=["authentication"], prefix="/users")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
async def home():
    return {"msg": "RescueLab Labeler"}


@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
