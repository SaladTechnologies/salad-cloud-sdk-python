from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_configuration_logging import ContainerConfigurationLogging
from .container_group_priority import ContainerGroupPriority
from .container_registry_authentication import ContainerRegistryAuthentication
from .create_container_resource_requirements import CreateContainerResourceRequirements


@JsonMap({})
class ContainerConfiguration(BaseModel):
    """Configuration for creating a container within a container group. Defines the container image, resource requirements, environment variables, and other settings needed to deploy and run the container.

    :param command: Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image. Each element in the array represents a command segment or argument., defaults to None
    :type command: List[str], optional
    :param environment_variables: Key-value pairs of environment variables to set within the container. These variables will be available to processes running inside the container., defaults to None
    :type environment_variables: dict, optional
    :param image: The container image.
    :type image: str
    :param image_caching: The container image caching., defaults to None
    :type image_caching: bool, optional
    :param logging: Configuration options for directing container logs to a logging provider. This schema enables you to specify a single logging destination for container output, supporting monitoring, debugging, and analytics use cases. Each provider has its own configuration parameters defined in the referenced schemas. Only one logging provider can be selected at a time., defaults to None
    :type logging: ContainerConfigurationLogging, optional
    :param priority: Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence., defaults to None
    :type priority: ContainerGroupPriority, optional
    :param registry_authentication: Authentication configuration for various container registry types, including AWS ECR, Docker Hub, GCP GAR, GCP GCR, and basic authentication., defaults to None
    :type registry_authentication: ContainerRegistryAuthentication, optional
    :param resources: Specifies the resource requirements for creating a container.
    :type resources: CreateContainerResourceRequirements
    """

    def __init__(
        self,
        image: str,
        resources: CreateContainerResourceRequirements,
        command: Union[List[str], None] = SENTINEL,
        environment_variables: dict = SENTINEL,
        image_caching: bool = SENTINEL,
        logging: ContainerConfigurationLogging = SENTINEL,
        priority: Union[ContainerGroupPriority, None] = SENTINEL,
        registry_authentication: ContainerRegistryAuthentication = SENTINEL,
        **kwargs,
    ):
        """Configuration for creating a container within a container group. Defines the container image, resource requirements, environment variables, and other settings needed to deploy and run the container.

        :param command: Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image. Each element in the array represents a command segment or argument., defaults to None
        :type command: List[str], optional
        :param environment_variables: Key-value pairs of environment variables to set within the container. These variables will be available to processes running inside the container., defaults to None
        :type environment_variables: dict, optional
        :param image: The container image.
        :type image: str
        :param image_caching: The container image caching., defaults to None
        :type image_caching: bool, optional
        :param logging: Configuration options for directing container logs to a logging provider. This schema enables you to specify a single logging destination for container output, supporting monitoring, debugging, and analytics use cases. Each provider has its own configuration parameters defined in the referenced schemas. Only one logging provider can be selected at a time., defaults to None
        :type logging: ContainerConfigurationLogging, optional
        :param priority: Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence., defaults to None
        :type priority: ContainerGroupPriority, optional
        :param registry_authentication: Authentication configuration for various container registry types, including AWS ECR, Docker Hub, GCP GAR, GCP GCR, and basic authentication., defaults to None
        :type registry_authentication: ContainerRegistryAuthentication, optional
        :param resources: Specifies the resource requirements for creating a container.
        :type resources: CreateContainerResourceRequirements
        """
        if command is not SENTINEL:
            self.command = command
        if environment_variables is not SENTINEL:
            self.environment_variables = environment_variables
        self.image = self._define_str(
            "image", image, pattern="^.*$", min_length=1, max_length=2048
        )
        if image_caching is not SENTINEL:
            self.image_caching = image_caching
        if logging is not SENTINEL:
            self.logging = self._define_object(logging, ContainerConfigurationLogging)
        if priority is not SENTINEL:
            self.priority = self._enum_matching(
                priority, ContainerGroupPriority.list(), "priority"
            )
        if registry_authentication is not SENTINEL:
            self.registry_authentication = self._define_object(
                registry_authentication, ContainerRegistryAuthentication
            )
        self.resources = self._define_object(
            resources, CreateContainerResourceRequirements
        )
        self._kwargs = kwargs
