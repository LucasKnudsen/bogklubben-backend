#!/usr/bin/env python3
import aws_cdk as cdk

from src.cdk.api_stack import ApiStack
from src.cdk.dynamo_stack import DynamoStack
from src.cdk.rekognition_stack import RekognitionStack

app = cdk.App()

dynamo_stack = DynamoStack(app, "DynamoStack")
api_stack = ApiStack(app, "ApiStack", user_table=dynamo_stack.user_table)
rekognition_stack = RekognitionStack(app, "RekognitionStack")
app.synth()
