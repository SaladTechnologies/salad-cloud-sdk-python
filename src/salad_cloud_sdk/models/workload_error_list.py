from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .workload_error import WorkloadError


@JsonMap({})
class WorkloadErrorList(BaseModel):
    """Represents a list of workload errors

    :param items: items
    :type items: List[WorkloadError]
    """

    def __init__(self, items: List[WorkloadError]):
        """Represents a list of workload errors

        :param items: items
        :type items: List[WorkloadError]
        """
        self.items = self._define_list(items, WorkloadError)
