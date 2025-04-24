from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_rekognition as rekognition


class RekognitionStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.collection = rekognition.CfnCollection(
            self, "RekognitionCollection", collection_id="bogklubben"
        )
