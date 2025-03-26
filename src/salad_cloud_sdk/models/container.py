from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_logging import ContainerLogging
from .container_resource_requirements import ContainerResourceRequirements


@JsonMap({})
class Container(BaseModel):
    """Represents a container with its configuration and resource requirements.

    :param command: List of commands to run inside the container. Each command is a string representing a command-line instruction.
    :type command: List[str]
    :param environment_variables: Environment variables to set in the container., defaults to None
    :type environment_variables: dict, optional
    :param hash: SHA-256 hash (64-character hexadecimal string), defaults to None
    :type hash: str, optional
    :param image: The container image.
    :type image: str
    :param image_caching: The container image caching., defaults to None
    :type image_caching: bool, optional
    :param logging: Configuration options for directing container logs to a logging provider. This schema enables you to specify a single logging destination for container output, supporting monitoring, debugging, and analytics use cases. Each provider has its own configuration parameters defined in the referenced schemas. Only one logging provider can be selected at a time., defaults to None
    :type logging: ContainerLogging, optional
    :param resources: Specifies the resource requirements for a container.
    :type resources: ContainerResourceRequirements
    :param size: Size of the container in bytes., defaults to None
    :type size: int, optional
    """

    def __init__(
        self,
        command: Union[List[str], None],
        image: str,
        resources: ContainerResourceRequirements,
        environment_variables: dict = SENTINEL,
        hash: str = SENTINEL,
        image_caching: bool = SENTINEL,
        logging: ContainerLogging = SENTINEL,
        size: int = SENTINEL,
        **kwargs,
    ):
        """Represents a container with its configuration and resource requirements.

        :param command: List of commands to run inside the container. Each command is a string representing a command-line instruction.
        :type command: List[str]
        :param environment_variables: Environment variables to set in the container., defaults to None
        :type environment_variables: dict, optional
        :param hash: SHA-256 hash (64-character hexadecimal string), defaults to None
        :type hash: str, optional
        :param image: The container image.
        :type image: str
        :param image_caching: The container image caching., defaults to None
        :type image_caching: bool, optional
        :param logging: Configuration options for directing container logs to a logging provider. This schema enables you to specify a single logging destination for container output, supporting monitoring, debugging, and analytics use cases. Each provider has its own configuration parameters defined in the referenced schemas. Only one logging provider can be selected at a time., defaults to None
        :type logging: ContainerLogging, optional
        :param resources: Specifies the resource requirements for a container.
        :type resources: ContainerResourceRequirements
        :param size: Size of the container in bytes., defaults to None
        :type size: int, optional
        """
        self.command = command
        if environment_variables is not SENTINEL:
            self.environment_variables = environment_variables
        if hash is not SENTINEL:
            self.hash = self._define_str(
                "hash",
                hash,
                pattern="^sha\d{1,3}:[a-fA-F0-9]{40,135}$",
                min_length=47,
                max_length=135,
            )
        self.image = self._define_str(
            "image", image, pattern="^.*$", min_length=1, max_length=2048
        )
        if image_caching is not SENTINEL:
            self.image_caching = image_caching
        if logging is not SENTINEL:
            self.logging = self._define_object(logging, ContainerLogging)
        self.resources = self._define_object(resources, ContainerResourceRequirements)
        if size is not SENTINEL:
            self.size = self._define_number("size", size, ge=0, le=9223372036854776000)
        self._kwargs = kwargs
