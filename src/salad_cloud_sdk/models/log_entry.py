from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .log_entry_resource import LogEntryResource
from .log_entry_severity import LogEntrySeverity


@JsonMap({"span_id": "span_Id", "trace_id": "trace_Id"})
class LogEntry(BaseModel):
    """LogEntry

    :param json_log: The log message in JSON format., defaults to None
    :type json_log: dict, optional
    :param parent_span_id: The parent span ID of the log entry, defaults to None
    :type parent_span_id: str, optional
    :param receive_time: The time when the log entry was received
    :type receive_time: str
    :param resource: The resource associated with the log entry
    :type resource: LogEntryResource
    :param severity: The severity level of the log entry
    :type severity: LogEntrySeverity
    :param span_id: The span ID of the log entry, defaults to None
    :type span_id: str, optional
    :param text_log: The log message in text format., defaults to None
    :type text_log: str, optional
    :param time: The timestamp of the log entry
    :type time: str
    :param trace_id: The trace ID of the log entry, defaults to None
    :type trace_id: str, optional
    """

    def __init__(
        self,
        receive_time: str,
        resource: LogEntryResource,
        severity: LogEntrySeverity,
        time: str,
        json_log: dict = SENTINEL,
        parent_span_id: str = SENTINEL,
        span_id: str = SENTINEL,
        text_log: str = SENTINEL,
        trace_id: str = SENTINEL,
        **kwargs,
    ):
        """LogEntry

        :param json_log: The log message in JSON format., defaults to None
        :type json_log: dict, optional
        :param parent_span_id: The parent span ID of the log entry, defaults to None
        :type parent_span_id: str, optional
        :param receive_time: The time when the log entry was received
        :type receive_time: str
        :param resource: The resource associated with the log entry
        :type resource: LogEntryResource
        :param severity: The severity level of the log entry
        :type severity: LogEntrySeverity
        :param span_id: The span ID of the log entry, defaults to None
        :type span_id: str, optional
        :param text_log: The log message in text format., defaults to None
        :type text_log: str, optional
        :param time: The timestamp of the log entry
        :type time: str
        :param trace_id: The trace ID of the log entry, defaults to None
        :type trace_id: str, optional
        """
        if json_log is not SENTINEL:
            self.json_log = json_log
        if parent_span_id is not SENTINEL:
            self.parent_span_id = self._define_str(
                "parent_span_id", parent_span_id, min_length=1, max_length=1000
            )
        self.receive_time = receive_time
        self.resource = self._define_object(resource, LogEntryResource)
        self.severity = self._enum_matching(
            severity, LogEntrySeverity.list(), "severity"
        )
        if span_id is not SENTINEL:
            self.span_id = self._define_str(
                "span_id", span_id, min_length=1, max_length=1000
            )
        if text_log is not SENTINEL:
            self.text_log = self._define_str("text_log", text_log, max_length=10000)
        self.time = time
        if trace_id is not SENTINEL:
            self.trace_id = self._define_str(
                "trace_id", trace_id, min_length=1, max_length=1000
            )
        self._kwargs = kwargs
