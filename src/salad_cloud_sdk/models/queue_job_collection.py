from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .queue_job import QueueJob


@JsonMap({})
class QueueJobCollection(BaseModel):
    """Represents a Queue Job Collection

    :param items: The list of queue jobs
    :type items: List[QueueJob]
    """

    def __init__(self, items: List[QueueJob], **kwargs):
        """Represents a Queue Job Collection

        :param items: The list of queue jobs
        :type items: List[QueueJob]
        """
        self.items = self._define_list(items, QueueJob)
        self._kwargs = kwargs
