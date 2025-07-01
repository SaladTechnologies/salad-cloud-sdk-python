from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .gpu_class import GpuClass


@JsonMap({})
class GpuClassesList(BaseModel):
    """Represents a list of GPU classes

    :param items: The list of GPU classes
    :type items: List[GpuClass]
    """

    def __init__(self, items: List[GpuClass], **kwargs):
        """Represents a list of GPU classes

        :param items: The list of GPU classes
        :type items: List[GpuClass]
        """
        self.items = self._define_list(items, GpuClass)
        self._kwargs = kwargs
