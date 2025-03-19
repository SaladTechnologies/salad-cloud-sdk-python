from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .workload_error import WorkloadError


@JsonMap({})
class WorkloadErrorList(BaseModel):
    """Represents a list of workload errors

    :param items: A list of workload errors
    :type items: List[WorkloadError]
    """

    def __init__(self, items: List[WorkloadError], **kwargs):
        """Represents a list of workload errors

        :param items: A list of workload errors
        :type items: List[WorkloadError]
        """
        self.items = self._define_list(items, WorkloadError)
        self._kwargs = kwargs
