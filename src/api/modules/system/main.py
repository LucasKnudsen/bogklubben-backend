from fastapi import APIRouter, Depends, HTTPException, Header, Body
from ...settings import settings
from .services.setup_recognition_service import create_collection

FIXED_COLLECTION_ID = settings.rekognition_collection_id


def authenticate_system_api_key(
    api_key: str = Header(default="", alias="X-System-Api-Key")
):
    print(api_key)
    if api_key != settings.system_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")


system_router = APIRouter(
    prefix="/system", dependencies=[Depends(authenticate_system_api_key)]
)


@system_router.get("/")
async def ping():
    return {"message": "Hello from system module"}


@system_router.post("/setup-rekognition")
async def setup_rekognition(
    collection_id: str | None = Body(default=FIXED_COLLECTION_ID, alias="collection_id")
):
    response = await create_collection(collection_id)
    return {"message": "Hello from setup-rekognition", "response": response}


@system_router.post("/index-face")
async def index_face():
    return {"message": "Hello from index-face"}
