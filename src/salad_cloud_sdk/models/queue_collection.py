from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .queue import Queue


@JsonMap({})
class QueueCollection(BaseModel):
    """Represents a Queue Collection

    :param items: The list of queues.
    :type items: List[Queue]
    """

    def __init__(self, items: List[Queue], **kwargs):
        """Represents a Queue Collection

        :param items: The list of queues.
        :type items: List[Queue]
        """
        self.items = self._define_list(items, Queue)
        self._kwargs = kwargs
