from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .queue_job_event import QueueJobEvent


class QueueJobStatus(Enum):
    """An enumeration representing different categories.

    :cvar PENDING: "pending"
    :vartype PENDING: str
    :cvar RUNNING: "running"
    :vartype RUNNING: str
    :cvar SUCCEEDED: "succeeded"
    :vartype SUCCEEDED: str
    :cvar CANCELLED: "cancelled"
    :vartype CANCELLED: str
    :cvar FAILED: "failed"
    :vartype FAILED: str
    """

    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    CANCELLED = "cancelled"
    FAILED = "failed"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, QueueJobStatus._member_map_.values()))


@JsonMap({"id_": "id"})
class QueueJob(BaseModel):
    """Represents a queue job

    :param create_time: The job creation time
    :type create_time: str
    :param events: The job events
    :type events: List[QueueJobEvent]
    :param id_: The job identifier
    :type id_: str
    :param input: The job input. May be any valid JSON.
    :type input: any
    :param metadata: Additional metadata for the job, defaults to None
    :type metadata: dict, optional
    :param output: The job output. May be any valid JSON., defaults to None
    :type output: any, optional
    :param status: The job status
    :type status: QueueJobStatus
    :param update_time: The job update time
    :type update_time: str
    :param webhook: The webhook URL to notify when the job completes, defaults to None
    :type webhook: str, optional
    """

    def __init__(
        self,
        create_time: str,
        events: List[QueueJobEvent],
        id_: str,
        input: any,
        status: QueueJobStatus,
        update_time: str,
        metadata: dict = SENTINEL,
        output: any = SENTINEL,
        webhook: str = SENTINEL,
        **kwargs,
    ):
        """Represents a queue job

        :param create_time: The job creation time
        :type create_time: str
        :param events: The job events
        :type events: List[QueueJobEvent]
        :param id_: The job identifier
        :type id_: str
        :param input: The job input. May be any valid JSON.
        :type input: any
        :param metadata: Additional metadata for the job, defaults to None
        :type metadata: dict, optional
        :param output: The job output. May be any valid JSON., defaults to None
        :type output: any, optional
        :param status: The job status
        :type status: QueueJobStatus
        :param update_time: The job update time
        :type update_time: str
        :param webhook: The webhook URL to notify when the job completes, defaults to None
        :type webhook: str, optional
        """
        self.create_time = self._define_str("create_time", create_time)
        self.events = self._define_list(events, QueueJobEvent)
        self.id_ = self._define_str("id_", id_)
        self.input = input
        if metadata is not SENTINEL:
            self.metadata = metadata
        if output is not SENTINEL:
            self.output = output
        self.status = self._enum_matching(status, QueueJobStatus.list(), "status")
        self.update_time = self._define_str("update_time", update_time)
        if webhook is not SENTINEL:
            self.webhook = self._define_str(
                "webhook",
                webhook,
                pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$",
                min_length=20,
                max_length=27,
            )
        self._kwargs = kwargs
