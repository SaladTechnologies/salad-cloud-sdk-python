from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .update_container_logging import UpdateContainerLogging
from .container_group_priority import ContainerGroupPriority
from .container_registry_authentication import ContainerRegistryAuthentication
from .container_resource_update_schema import ContainerResourceUpdateSchema


@JsonMap({})
class UpdateContainer(BaseModel):
    """Represents an update container object

    :param command: Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image., defaults to None
    :type command: List[str], optional
    :param environment_variables: Environment variables to set in the container., defaults to None
    :type environment_variables: dict, optional
    :param image: The container image to use., defaults to None
    :type image: str, optional
    :param image_caching: The container image caching., defaults to None
    :type image_caching: bool, optional
    :param logging: Configuration options for directing container logs to a logging provider. This schema enables you to specify a single logging destination for container output, supporting monitoring, debugging, and analytics use cases. Each provider has its own configuration parameters defined in the referenced schemas. Only one logging provider can be selected at a time., defaults to None
    :type logging: UpdateContainerLogging, optional
    :param priority: Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence., defaults to None
    :type priority: ContainerGroupPriority, optional
    :param registry_authentication: Authentication configuration for various container registry types, including AWS ECR, Docker Hub, GCP GAR, GCP GCR, and basic authentication., defaults to None
    :type registry_authentication: ContainerRegistryAuthentication, optional
    :param resources: Defines the resource specifications that can be modified for a container group, including CPU, memory, GPU classes, and storage allocations., defaults to None
    :type resources: ContainerResourceUpdateSchema, optional
    """

    def __init__(
        self,
        command: Union[List[str], None] = SENTINEL,
        environment_variables: dict = SENTINEL,
        image: Union[str, None] = SENTINEL,
        image_caching: bool = SENTINEL,
        logging: Union[UpdateContainerLogging, None] = SENTINEL,
        priority: Union[ContainerGroupPriority, None] = SENTINEL,
        registry_authentication: ContainerRegistryAuthentication = SENTINEL,
        resources: Union[ContainerResourceUpdateSchema, None] = SENTINEL,
        **kwargs,
    ):
        """Represents an update container object

        :param command: Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image., defaults to None
        :type command: List[str], optional
        :param environment_variables: Environment variables to set in the container., defaults to None
        :type environment_variables: dict, optional
        :param image: The container image to use., defaults to None
        :type image: str, optional
        :param image_caching: The container image caching., defaults to None
        :type image_caching: bool, optional
        :param logging: Configuration options for directing container logs to a logging provider. This schema enables you to specify a single logging destination for container output, supporting monitoring, debugging, and analytics use cases. Each provider has its own configuration parameters defined in the referenced schemas. Only one logging provider can be selected at a time., defaults to None
        :type logging: UpdateContainerLogging, optional
        :param priority: Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence., defaults to None
        :type priority: ContainerGroupPriority, optional
        :param registry_authentication: Authentication configuration for various container registry types, including AWS ECR, Docker Hub, GCP GAR, GCP GCR, and basic authentication., defaults to None
        :type registry_authentication: ContainerRegistryAuthentication, optional
        :param resources: Defines the resource specifications that can be modified for a container group, including CPU, memory, GPU classes, and storage allocations., defaults to None
        :type resources: ContainerResourceUpdateSchema, optional
        """
        if command is not SENTINEL:
            self.command = command
        if environment_variables is not SENTINEL:
            self.environment_variables = environment_variables
        if image is not SENTINEL:
            self.image = self._define_str(
                "image",
                image,
                nullable=True,
                pattern="^.*$",
                min_length=1,
                max_length=1024,
            )
        if image_caching is not SENTINEL:
            self.image_caching = image_caching
        if logging is not SENTINEL:
            self.logging = self._define_object(logging, UpdateContainerLogging)
        if priority is not SENTINEL:
            self.priority = self._enum_matching(
                priority, ContainerGroupPriority.list(), "priority"
            )
        if registry_authentication is not SENTINEL:
            self.registry_authentication = self._define_object(
                registry_authentication, ContainerRegistryAuthentication
            )
        if resources is not SENTINEL:
            self.resources = self._define_object(
                resources, ContainerResourceUpdateSchema
            )
        self._kwargs = kwargs
