from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group_instance import ContainerGroupInstance


@JsonMap({})
class ContainerGroupInstances(BaseModel):
    """Represents a list of container group instances

    :param instances: instances
    :type instances: List[ContainerGroupInstance]
    """

    def __init__(self, instances: List[ContainerGroupInstance]):
        """Represents a list of container group instances

        :param instances: instances
        :type instances: List[ContainerGroupInstance]
        """
        self.instances = self._define_list(instances, ContainerGroupInstance)
