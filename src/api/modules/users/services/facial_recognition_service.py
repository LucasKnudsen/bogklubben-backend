import boto3
import json
from ....settings import settings
from fastapi import HTTPException, UploadFile, File
from ....shared import async_timer

rekognition = boto3.client(
    "rekognition",
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)

COLLECTION_ID = settings.rekognition_collection_id


@async_timer
async def face_login(file: UploadFile = File(...)) -> str:
    """
    Args:
        file: UploadFile - The image file to search for a face in.

    Returns:
        str - The user ID of the person in the image.
    """

    image_bytes = await file.read()

    response = rekognition.search_faces_by_image(
        CollectionId=COLLECTION_ID,
        Image={"Bytes": image_bytes},
        FaceMatchThreshold=80,
        MaxFaces=1,
    )

    print(json.dumps(response, indent=2))

    if response["FaceMatches"]:
        user_id = response["FaceMatches"][0]["Face"]["ExternalImageId"]
        return user_id

    raise HTTPException(status_code=401, detail="No face matches found")
