from __future__ import annotations
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_registry_authentication_aws_ecr import (
    ContainerRegistryAuthenticationAwsEcr,
)
from .container_registry_authentication_basic import (
    ContainerRegistryAuthenticationBasic,
)
from .container_registry_authentication_docker_hub import (
    ContainerRegistryAuthenticationDockerHub,
)
from .container_registry_authentication_gcp_gar import (
    ContainerRegistryAuthenticationGcpGar,
)
from .container_registry_authentication_gcp_gcr import (
    ContainerRegistryAuthenticationGcpGcr,
)


@JsonMap({})
class ContainerRegistryAuthentication(BaseModel):
    """Authentication configuration for various container registry types, including AWS ECR, Docker Hub, GCP GAR, GCP GCR, and basic authentication.

    :param aws_ecr: Authentication details for AWS Elastic Container Registry (ECR), defaults to None
    :type aws_ecr: ContainerRegistryAuthenticationAwsEcr, optional
    :param basic: Basic username and password authentication for generic container registries, defaults to None
    :type basic: ContainerRegistryAuthenticationBasic, optional
    :param docker_hub: Authentication details for Docker Hub registry, defaults to None
    :type docker_hub: ContainerRegistryAuthenticationDockerHub, optional
    :param gcp_gar: Authentication details for Google Artifact Registry (GAR), defaults to None
    :type gcp_gar: ContainerRegistryAuthenticationGcpGar, optional
    :param gcp_gcr: Authentication details for Google Container Registry (GCR), defaults to None
    :type gcp_gcr: ContainerRegistryAuthenticationGcpGcr, optional
    """

    def __init__(
        self,
        aws_ecr: Union[ContainerRegistryAuthenticationAwsEcr, None] = SENTINEL,
        basic: ContainerRegistryAuthenticationBasic = SENTINEL,
        docker_hub: ContainerRegistryAuthenticationDockerHub = SENTINEL,
        gcp_gar: ContainerRegistryAuthenticationGcpGar = SENTINEL,
        gcp_gcr: ContainerRegistryAuthenticationGcpGcr = SENTINEL,
        **kwargs,
    ):
        """Authentication configuration for various container registry types, including AWS ECR, Docker Hub, GCP GAR, GCP GCR, and basic authentication.

        :param aws_ecr: Authentication details for AWS Elastic Container Registry (ECR), defaults to None
        :type aws_ecr: ContainerRegistryAuthenticationAwsEcr, optional
        :param basic: Basic username and password authentication for generic container registries, defaults to None
        :type basic: ContainerRegistryAuthenticationBasic, optional
        :param docker_hub: Authentication details for Docker Hub registry, defaults to None
        :type docker_hub: ContainerRegistryAuthenticationDockerHub, optional
        :param gcp_gar: Authentication details for Google Artifact Registry (GAR), defaults to None
        :type gcp_gar: ContainerRegistryAuthenticationGcpGar, optional
        :param gcp_gcr: Authentication details for Google Container Registry (GCR), defaults to None
        :type gcp_gcr: ContainerRegistryAuthenticationGcpGcr, optional
        """
        if aws_ecr is not SENTINEL:
            self.aws_ecr = self._define_object(
                aws_ecr, ContainerRegistryAuthenticationAwsEcr
            )
        if basic is not SENTINEL:
            self.basic = self._define_object(
                basic, ContainerRegistryAuthenticationBasic
            )
        if docker_hub is not SENTINEL:
            self.docker_hub = self._define_object(
                docker_hub, ContainerRegistryAuthenticationDockerHub
            )
        if gcp_gar is not SENTINEL:
            self.gcp_gar = self._define_object(
                gcp_gar, ContainerRegistryAuthenticationGcpGar
            )
        if gcp_gcr is not SENTINEL:
            self.gcp_gcr = self._define_object(
                gcp_gcr, ContainerRegistryAuthenticationGcpGcr
            )
        self._kwargs = kwargs
