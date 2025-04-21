# src/api/main.py
from fastapi import FastAPI, APIRouter

app = FastAPI()

quiz_router = APIRouter()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running on AWS Fargate!"}
