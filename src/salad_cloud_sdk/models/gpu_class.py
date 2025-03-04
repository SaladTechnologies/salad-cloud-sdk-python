from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .gpu_class_price import GpuClassPrice


@JsonMap({"id_": "id"})
class GpuClass(BaseModel):
    """Represents a GPU Class

    :param id_: The unique identifier
    :type id_: str
    :param name: The GPU class name
    :type name: str
    :param prices: The list of prices for each container group priority
    :type prices: List[GpuClassPrice]
    :param is_high_demand: Whether the GPU class is in high demand, defaults to None
    :type is_high_demand: bool, optional
    """

    def __init__(
        self,
        id_: str,
        name: str,
        prices: List[GpuClassPrice],
        is_high_demand: bool = SENTINEL,
        **kwargs,
    ):
        """Represents a GPU Class

        :param id_: The unique identifier
        :type id_: str
        :param name: The GPU class name
        :type name: str
        :param prices: The list of prices for each container group priority
        :type prices: List[GpuClassPrice]
        :param is_high_demand: Whether the GPU class is in high demand, defaults to None
        :type is_high_demand: bool, optional
        """
        self.id_ = id_
        self.name = self._define_str(
            "name", name, pattern="^[ -~]{2,63}$", min_length=2, max_length=63
        )
        self.prices = self._define_list(prices, GpuClassPrice)
        if is_high_demand is not SENTINEL:
            self.is_high_demand = is_high_demand
        self._kwargs = kwargs
