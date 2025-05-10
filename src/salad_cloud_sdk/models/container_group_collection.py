from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group import ContainerGroup


@JsonMap({})
class ContainerGroupCollection(BaseModel):
    """A paginated collection of container groups that provides a structured way to access multiple container group resources in a single response.

    :param items: An array containing container group objects. Each object represents a discrete container group with its own properties, configuration, and status.
    :type items: List[ContainerGroup]
    """

    def __init__(self, items: List[ContainerGroup], **kwargs):
        """A paginated collection of container groups that provides a structured way to access multiple container group resources in a single response.

        :param items: An array containing container group objects. Each object represents a discrete container group with its own properties, configuration, and status.
        :type items: List[ContainerGroup]
        """
        self.items = self._define_list(items, ContainerGroup)
        self._kwargs = kwargs
