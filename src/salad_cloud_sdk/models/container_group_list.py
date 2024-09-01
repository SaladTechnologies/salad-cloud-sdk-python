from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group import ContainerGroup


@JsonMap({})
class ContainerGroupList(BaseModel):
    """Represents a list of container groups

    :param items: items
    :type items: List[ContainerGroup]
    """

    def __init__(self, items: List[ContainerGroup]):
        """Represents a list of container groups

        :param items: items
        :type items: List[ContainerGroup]
        """
        self.items = self._define_list(items, ContainerGroup)
