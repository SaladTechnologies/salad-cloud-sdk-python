from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .country_code import CountryCode


@JsonMap({})
class GpuAvailabilityPrototype(BaseModel):
    """GpuAvailabilityPrototype

    :param country_codes: A list of country codes where the resources are available, defaults to None
    :type country_codes: List[CountryCode], optional
    :param cpu: The number of available CPU cores, defaults to None
    :type cpu: int, optional
    :param gpu_classes: A list of available GPU class names
    :type gpu_classes: List[str]
    :param memory: The amount of available memory in MB, defaults to None
    :type memory: int, optional
    :param storage_amount: The amount of available storage in bytes, defaults to None
    :type storage_amount: int, optional
    """

    def __init__(
        self,
        gpu_classes: List[str],
        country_codes: List[CountryCode] = SENTINEL,
        cpu: Union[int, None] = SENTINEL,
        memory: Union[int, None] = SENTINEL,
        storage_amount: Union[int, None] = SENTINEL,
        **kwargs,
    ):
        """GpuAvailabilityPrototype

        :param country_codes: A list of country codes where the resources are available, defaults to None
        :type country_codes: List[CountryCode], optional
        :param cpu: The number of available CPU cores, defaults to None
        :type cpu: int, optional
        :param gpu_classes: A list of available GPU class names
        :type gpu_classes: List[str]
        :param memory: The amount of available memory in MB, defaults to None
        :type memory: int, optional
        :param storage_amount: The amount of available storage in bytes, defaults to None
        :type storage_amount: int, optional
        """
        if country_codes is not SENTINEL:
            self.country_codes = self._define_list(country_codes, CountryCode)
        if cpu is not SENTINEL:
            self.cpu = self._define_number("cpu", cpu, nullable=True)
        self.gpu_classes = gpu_classes
        if memory is not SENTINEL:
            self.memory = self._define_number("memory", memory, nullable=True)
        if storage_amount is not SENTINEL:
            self.storage_amount = self._define_number(
                "storage_amount", storage_amount, nullable=True
            )
        self._kwargs = kwargs
