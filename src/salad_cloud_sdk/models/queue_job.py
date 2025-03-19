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

    :param id_: The job identifier
    :type id_: str
    :param input: The job input. May be any valid JSON.
    :type input: any
    :param metadata: Additional metadata for the job, defaults to None
    :type metadata: dict, optional
    :param webhook: The webhook URL to notify when the job completes, defaults to None
    :type webhook: str, optional
    :param status: The job status
    :type status: QueueJobStatus
    :param events: The job events
    :type events: List[QueueJobEvent]
    :param output: The job output. May be any valid JSON., defaults to None
    :type output: any, optional
    :param create_time: The job creation time
    :type create_time: str
    :param update_time: The job update time
    :type update_time: str
    """

    def __init__(
        self,
        id_: str,
        input: any,
        status: QueueJobStatus,
        events: List[QueueJobEvent],
        create_time: str,
        update_time: str,
        metadata: dict = SENTINEL,
        webhook: str = SENTINEL,
        output: any = SENTINEL,
        **kwargs,
    ):
        """Represents a queue job

        :param id_: The job identifier
        :type id_: str
        :param input: The job input. May be any valid JSON.
        :type input: any
        :param metadata: Additional metadata for the job, defaults to None
        :type metadata: dict, optional
        :param webhook: The webhook URL to notify when the job completes, defaults to None
        :type webhook: str, optional
        :param status: The job status
        :type status: QueueJobStatus
        :param events: The job events
        :type events: List[QueueJobEvent]
        :param output: The job output. May be any valid JSON., defaults to None
        :type output: any, optional
        :param create_time: The job creation time
        :type create_time: str
        :param update_time: The job update time
        :type update_time: str
        """
        self.id_ = id_
        self.input = input
        if metadata is not SENTINEL:
            self.metadata = metadata
        if webhook is not SENTINEL:
            self.webhook = self._define_str(
                "webhook",
                webhook,
                pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$",
                min_length=20,
                max_length=27,
            )
        self.status = self._enum_matching(status, QueueJobStatus.list(), "status")
        self.events = self._define_list(events, QueueJobEvent)
        if output is not SENTINEL:
            self.output = output
        self.create_time = create_time
        self.update_time = update_time
        self._kwargs = kwargs
