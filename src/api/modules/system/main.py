from fastapi import APIRouter, Depends, HTTPException, Header, Body, File, UploadFile
from ...settings import settings
from .services.setup_recognition_service import (
    create_collection,
    index_face as _index_face,
)
from ...shared import APIResponse

FIXED_COLLECTION_ID = settings.rekognition_collection_id


def authenticate_system_api_key(
    api_key: str = Header(default="", alias="X-System-Api-Key")
):
    if api_key != settings.system_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")


system_router = APIRouter(
    prefix="/system", dependencies=[Depends(authenticate_system_api_key)]
)


@system_router.post("/setup-rekognition")
async def setup_rekognition(
    collection_id: str | None = Body(default=FIXED_COLLECTION_ID, alias="collection_id")
):
    response = await create_collection(collection_id)
    return APIResponse(message="Hello from setup-rekognition", data=response)


@system_router.post("/index-face")
async def index_face(
    image: UploadFile = File(...),
    user_id: str = Body(..., alias="user_id"),
    collection_id: str | None = Body(
        default=FIXED_COLLECTION_ID, alias="collection_id"
    ),
):
    response = await _index_face(image, user_id, collection_id)
    return APIResponse(message="Hello from index-face", data=response)


# Example curl command to index a face
# curl --location 'http://127.0.0.1:8080/system/index-face' \
# --header 'X-System-Api-Key: eaffc4fd-91db-4740-bfd3-e71f53906ef9' \
# --form 'image=@".local/winblad.jpeg"' \
# --form 'user_id="winblad"'
