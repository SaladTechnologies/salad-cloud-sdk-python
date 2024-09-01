from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .queue_job import QueueJob


@JsonMap({})
class QueueJobList(BaseModel):
    """Represents a list of queue jobs

    :param items: items
    :type items: List[QueueJob]
    """

    def __init__(self, items: List[QueueJob]):
        """Represents a list of queue jobs

        :param items: items
        :type items: List[QueueJob]
        """
        self.items = self._define_list(items, QueueJob)
