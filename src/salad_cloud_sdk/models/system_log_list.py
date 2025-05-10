from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .system_log import SystemLog


@JsonMap({})
class SystemLogList(BaseModel):
    """Represents a list of system logs

    :param items: A list of system logs
    :type items: List[SystemLog]
    """

    def __init__(self, items: List[SystemLog], **kwargs):
        """Represents a list of system logs

        :param items: A list of system logs
        :type items: List[SystemLog]
        """
        self.items = self._define_list(items, SystemLog)
        self._kwargs = kwargs
