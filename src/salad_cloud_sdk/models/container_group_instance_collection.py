from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group_instance import ContainerGroupInstance


@JsonMap({})
class ContainerGroupInstanceCollection(BaseModel):
    """A collection of container group instances returned as part of a paginated response or batch operation result.

    :param instances: An array of container group instances, each representing a deployed container group with its current state and configuration information.
    :type instances: List[ContainerGroupInstance]
    """

    def __init__(self, instances: List[ContainerGroupInstance], **kwargs):
        """A collection of container group instances returned as part of a paginated response or batch operation result.

        :param instances: An array of container group instances, each representing a deployed container group with its current state and configuration information.
        :type instances: List[ContainerGroupInstance]
        """
        self.instances = self._define_list(instances, ContainerGroupInstance)
        self._kwargs = kwargs
