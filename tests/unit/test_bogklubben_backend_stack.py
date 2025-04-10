import aws_cdk as core
import aws_cdk.assertions as assertions

from bogklubben_backend.bogklubben_backend_stack import BogklubbenBackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in bogklubben_backend/bogklubben_backend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BogklubbenBackendStack(app, "bogklubben-backend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
