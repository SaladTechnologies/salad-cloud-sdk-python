from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .log_entry_query_sort_order import LogEntryQuerySortOrder


@JsonMap({})
class LogEntryQuery(BaseModel):
    """Represents a query for logs

    :param end_time: The end time of the time range
    :type end_time: str
    :param page_size: The maximum number of items per page., defaults to None
    :type page_size: int, optional
    :param query: The query string for filtering logs
    :type query: str
    :param sort_order: The sort order of the log entries. `asc` will sort the log entries in chronological order. `desc` will sort the log entries in reverse chronological order., defaults to None
    :type sort_order: LogEntryQuerySortOrder, optional
    :param start_time: The start time of the time range
    :type start_time: str
    """

    def __init__(
        self,
        end_time: str,
        query: str,
        start_time: str,
        page_size: int = SENTINEL,
        sort_order: LogEntryQuerySortOrder = SENTINEL,
        **kwargs,
    ):
        """Represents a query for logs

        :param end_time: The end time of the time range
        :type end_time: str
        :param page_size: The maximum number of items per page., defaults to None
        :type page_size: int, optional
        :param query: The query string for filtering logs
        :type query: str
        :param sort_order: The sort order of the log entries. `asc` will sort the log entries in chronological order. `desc` will sort the log entries in reverse chronological order., defaults to None
        :type sort_order: LogEntryQuerySortOrder, optional
        :param start_time: The start time of the time range
        :type start_time: str
        """
        self.end_time = end_time
        if page_size is not SENTINEL:
            self.page_size = self._define_number("page_size", page_size, ge=1, le=100)
        self.query = self._define_str("query", query, max_length=20000)
        if sort_order is not SENTINEL:
            self.sort_order = self._enum_matching(
                sort_order, LogEntryQuerySortOrder.list(), "sort_order"
            )
        self.start_time = start_time
        self._kwargs = kwargs
