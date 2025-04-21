from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_ecr_assets as ecr_assets,
)
from constructs import Construct
import os

class ApiStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
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
            directory=os.path.join(os.path.dirname(__file__), "../api")
        )

        # Create a Fargate service with an Application Load Balancer.
        # The ALB pattern sets up a listener, target group, and routes requests to your service.
        ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "ApiFargateService",
            cluster=cluster,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_docker_image_asset(api_docker_image),
                container_port=8080  # Adjust if your FastAPI app serves on a different port
            ),
            public_load_balancer=True,
            cpu=256,
            memory_limit_mib=512,
        )


