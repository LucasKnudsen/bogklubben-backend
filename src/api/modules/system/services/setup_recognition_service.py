from ....settings import settings
import boto3

COLLECTION_ID = settings.rekognition_collection_id

rekognition = boto3.client(
    "rekognition",
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)


async def create_collection():
    response = rekognition.create_collection(CollectionId=COLLECTION_ID)
    return response


async def index_faces(file, user_id):
    image_bytes = await file.read()
    response = rekognition.index_faces(
        CollectionId=COLLECTION_ID,
        Image={"Bytes": image_bytes},
        ExternalImageId=user_id,
    )
    return response
