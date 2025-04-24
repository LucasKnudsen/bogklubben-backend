from fastapi import APIRouter, Request, UploadFile, File
from .services.facial_recognition_service import face_login
from ...shared import APIResponse

users_router = APIRouter()


@users_router.post("/login")
async def login(request: Request, image: UploadFile = File(...)):
    result = await face_login(image)
    return APIResponse(message="Hello, World!", data=result)
