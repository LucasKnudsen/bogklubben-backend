import boto3
import os
from ....settings import settings

rekognition = boto3.client(
    "rekognition",
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)

COLLECTION_ID = settings.rekognition_collection_id


async def face_login(file):
    image_bytes = await file.read()

    response = rekognition.search_faces_by_image(
        CollectionId=COLLECTION_ID,
        Image={"Bytes": image_bytes},
        FaceMatchThreshold=80,
        MaxFaces=1,
    )

    print(response)
    return response
