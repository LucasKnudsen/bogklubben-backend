from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_ecr_assets as ecr_assets,
    aws_dynamodb as dynamodb,
)
from constructs import Construct
import os


class ApiStack(Stack):
    def __init__(
        self, scope: Construct, id: str, user_table: dynamodb.TableV2, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a new VPC spanning two AZs (using defaults)
        vpc = ec2.Vpc(self, "ApiVpc", max_azs=2)

        # Create an ECS cluster within the VPC
        cluster = ecs.Cluster(self, "ApiCluster", vpc=vpc)

        # Build a Docker image from the FastAPI application's directory.
        # This assumes your Dockerfile is located in the src/api folder.
        api_docker_image = ecr_assets.DockerImageAsset(
            self,
            "ApiImage",
            directory=os.path.join(os.path.dirname(__file__), "../api"),
        )

        # Create a Fargate service with an Application Load Balancer.
        # The ALB pattern sets up a listener, target group, and routes requests to your service.
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "ApiFargateService",
            cluster=cluster,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_docker_image_asset(api_docker_image),
                container_port=8080,
            ),
            public_load_balancer=True,
            cpu=256,
            memory_limit_mib=512,
        )

        container = fargate_service.task_definition.default_container
        container.add_environment("REKOGNITION_COLLECTION_ID", "")
        container.add_environment("AWS_REGION", "eu-west-1")

        user_table.grant_read_write_data(fargate_service.task_definition.task_role)
