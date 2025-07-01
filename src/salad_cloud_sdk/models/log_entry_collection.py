from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .log_entry import LogEntry


@JsonMap({})
class LogEntryCollection(BaseModel):
    """Represents a page of organization logs

    :param items: A collection of log entries
    :type items: List[LogEntry]
    :param organization_name: The organization name.
    :type organization_name: str
    :param page_max_time: The maximum time page boundary. This may be used when getting paginated results.
    :type page_max_time: str
    :param page_min_time: The minimum time page boundary. This may be used when getting paginated results.
    :type page_min_time: str
    """

    def __init__(
        self,
        items: List[LogEntry],
        organization_name: str,
        page_max_time: str,
        page_min_time: str,
        **kwargs,
    ):
        """Represents a page of organization logs

        :param items: A collection of log entries
        :type items: List[LogEntry]
        :param organization_name: The organization name.
        :type organization_name: str
        :param page_max_time: The maximum time page boundary. This may be used when getting paginated results.
        :type page_max_time: str
        :param page_min_time: The minimum time page boundary. This may be used when getting paginated results.
        :type page_min_time: str
        """
        self.items = self._define_list(items, LogEntry)
        self.organization_name = self._define_str(
            "organization_name",
            organization_name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.page_max_time = page_max_time
        self.page_min_time = page_min_time
        self._kwargs = kwargs
