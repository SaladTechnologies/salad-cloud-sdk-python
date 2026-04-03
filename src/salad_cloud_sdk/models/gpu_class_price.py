from __future__ import annotations
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group_priority import ContainerGroupPriority


@JsonMap({})
class GpuClassPrice(BaseModel):
    """Represents the price of a GPU class for a given container group priority

    :param price: The price
    :type price: str
    :param priority: Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence.
    :type priority: ContainerGroupPriority
    """

    def __init__(
        self, price: str, priority: Union[ContainerGroupPriority, None], **kwargs
    ):
        """Represents the price of a GPU class for a given container group priority

        :param price: The price
        :type price: str
        :param priority: Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence.
        :type priority: ContainerGroupPriority
        """
        self.price = self._define_str(
            "price", price, pattern="^.*$", min_length=1, max_length=20
        )
        self.priority = self._enum_matching(
            priority, ContainerGroupPriority.list(), "priority", nullable=True
        )
        self._kwargs = kwargs
