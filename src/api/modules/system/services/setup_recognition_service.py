from ....settings import settings
import boto3
from fastapi import UploadFile

rekognition = boto3.client(
    "rekognition",
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)


async def create_collection(collection_id: str):
    response = rekognition.create_collection(CollectionId=collection_id)
    return response


async def index_face(file: UploadFile, user_id: str, collection_id: str):
    image_bytes = await file.read()
    response = rekognition.index_faces(
        CollectionId=collection_id,
        Image={"Bytes": image_bytes},
        ExternalImageId=user_id,
    )
    return response
