from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group_priority import ContainerGroupPriority


@JsonMap({})
class GpuClassPrice(BaseModel):
    """Represents the price of a GPU class for a given container group priority

    :param priority: priority
    :type priority: ContainerGroupPriority
    :param price: The price
    :type price: str
    """

    def __init__(self, priority: ContainerGroupPriority, price: str):
        """Represents the price of a GPU class for a given container group priority

        :param priority: priority
        :type priority: ContainerGroupPriority
        :param price: The price
        :type price: str
        """
        self.priority = self._enum_matching(
            priority, ContainerGroupPriority.list(), "priority"
        )
        self.price = self._define_str("price", price, min_length=1, max_length=20)
