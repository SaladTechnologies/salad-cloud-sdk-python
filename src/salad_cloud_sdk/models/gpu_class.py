from __future__ import annotations
from enum import Enum
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .gpu_class_price import GpuClassPrice


class GpuClassType(Enum):
    """An enumeration representing different categories.

    :cvar COMMUNITY: "community"
    :vartype COMMUNITY: str
    :cvar SECURE: "secure"
    :vartype SECURE: str
    """

    COMMUNITY = "community"
    SECURE = "secure"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GpuClassType._member_map_.values()))


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
    :param gpu_class_type: The type of GPU class, defaults to None
    :type gpu_class_type: GpuClassType, optional
    :param min_vcpu: The minimum vCPU count, defaults to None
    :type min_vcpu: int, optional
    :param max_vcpu: The maximum vCPU count, defaults to None
    :type max_vcpu: int, optional
    :param min_ram: The minimum RAM amount in GB, defaults to None
    :type min_ram: int, optional
    :param max_ram: The maximum RAM amount in GB, defaults to None
    :type max_ram: int, optional
    :param min_storage: The minimum storage amount in GB, defaults to None
    :type min_storage: int, optional
    :param max_storage: The maximum storage amount in GB, defaults to None
    :type max_storage: int, optional
    """

    def __init__(
        self,
        id_: str,
        name: str,
        prices: List[GpuClassPrice],
        is_high_demand: bool = SENTINEL,
        gpu_class_type: GpuClassType = SENTINEL,
        min_vcpu: int = SENTINEL,
        max_vcpu: int = SENTINEL,
        min_ram: int = SENTINEL,
        max_ram: int = SENTINEL,
        min_storage: int = SENTINEL,
        max_storage: int = SENTINEL,
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
        :param gpu_class_type: The type of GPU class, defaults to None
        :type gpu_class_type: GpuClassType, optional
        :param min_vcpu: The minimum vCPU count, defaults to None
        :type min_vcpu: int, optional
        :param max_vcpu: The maximum vCPU count, defaults to None
        :type max_vcpu: int, optional
        :param min_ram: The minimum RAM amount in GB, defaults to None
        :type min_ram: int, optional
        :param max_ram: The maximum RAM amount in GB, defaults to None
        :type max_ram: int, optional
        :param min_storage: The minimum storage amount in GB, defaults to None
        :type min_storage: int, optional
        :param max_storage: The maximum storage amount in GB, defaults to None
        :type max_storage: int, optional
        """
        self.id_ = id_
        self.name = self._define_str(
            "name", name, pattern="^[ -~]{2,63}$", min_length=2, max_length=63
        )
        self.prices = self._define_list(prices, GpuClassPrice)
        if is_high_demand is not SENTINEL:
            self.is_high_demand = is_high_demand
        if gpu_class_type is not SENTINEL:
            self.gpu_class_type = self._enum_matching(
                gpu_class_type, GpuClassType.list(), "gpu_class_type"
            )
        if min_vcpu is not SENTINEL:
            self.min_vcpu = self._define_number("min_vcpu", min_vcpu, ge=0)
        if max_vcpu is not SENTINEL:
            self.max_vcpu = max_vcpu
        if min_ram is not SENTINEL:
            self.min_ram = self._define_number("min_ram", min_ram, ge=0)
        if max_ram is not SENTINEL:
            self.max_ram = max_ram
        if min_storage is not SENTINEL:
            self.min_storage = self._define_number("min_storage", min_storage, ge=0)
        if max_storage is not SENTINEL:
            self.max_storage = max_storage
        self._kwargs = kwargs
