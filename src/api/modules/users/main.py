from fastapi import APIRouter, UploadFile, File
from .services.facial_recognition_service import face_login
from ...shared import APIResponse

users_router = APIRouter()


@users_router.post("/login")
async def login(image: UploadFile = File(...)):
    user_id = await face_login(image)

    # TODO: Implement the logic to login the user
    # - Check data entity
    # - Generate a JWT token
    # - Return the JWT token

    return APIResponse(message="Hello, World!", data=user_id)
