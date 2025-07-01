from typing import Awaitable, Union
from .utils.to_async import to_async
from ..logs import LogsService
from ...models import LogEntryCollection, LogEntryQuery


class LogsServiceAsync(LogsService):
    """
    Async Wrapper for LogsServiceAsync
    """

    def query_log_entries(
        self, request_body: LogEntryQuery, organization_name: str
    ) -> Awaitable[LogEntryCollection]:
        return to_async(super().query_log_entries)(request_body, organization_name)
