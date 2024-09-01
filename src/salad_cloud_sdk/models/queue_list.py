from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .queue import Queue


@JsonMap({})
class QueueList(BaseModel):
    """Represents a list of queues

    :param items: items
    :type items: List[Queue]
    """

    def __init__(self, items: List[Queue]):
        """Represents a list of queues

        :param items: items
        :type items: List[Queue]
        """
        self.items = self._define_list(items, Queue)
