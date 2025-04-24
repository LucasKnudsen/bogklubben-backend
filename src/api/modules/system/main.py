from fastapi import APIRouter, Depends

system_router = APIRouter(prefix="/system", dependencies=[Depends()])


@system_router.get("/")
async def ping():
    return {"message": "Hello from system module"}


@system_router.post("/setup-recognition")
async def setup_recognition():
    return {"message": "Hello from system module"}


@system_router.post("/index-face")
async def setup_recognition():
    return {"message": "Hello from system module"}
