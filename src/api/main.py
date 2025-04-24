# src/api/main.py
from fastapi import FastAPI
from .modules.users.main import users_router


app = FastAPI(title="Bogklubben API", version="1.0.0", description="Bogklubben API")


app.include_router(users_router)


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running on AWS Fargate!"}
