# src/api/main.py
from fastapi import FastAPI, HTTPException
from botocore.errorfactory import ClientError
from .modules.users.main import users_router
from .modules.system.main import system_router
from .shared import (
    global_exception_handler,
    global_http_exception_handler,
    boto_client_error_handler,
)

app = FastAPI(title="Bogklubben API", version="1.0.0", description="Bogklubben API")

app.add_exception_handler(HTTPException, global_http_exception_handler)
app.add_exception_handler(ClientError, boto_client_error_handler)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(users_router)
app.include_router(system_router)


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running on AWS Fargate!"}
