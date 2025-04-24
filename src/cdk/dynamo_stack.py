from aws_cdk import Stack, CfnOutput
from constructs import Construct
from aws_cdk import aws_dynamodb as dynamodb


class DynamoStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a new DynamoDB table
        self.user_table = dynamodb.TableV2(
            self,
            "UserTable",
            table_name="UserTable",
            partition_key=dynamodb.Attribute(
                name="id", type=dynamodb.AttributeType.STRING
            ),
            billing=dynamodb.Billing.on_demand(),
        )

        CfnOutput(
            self,
            "UserTableName",
            value=self.user_table.table_name,
            export_name="UserTableName",
        )
