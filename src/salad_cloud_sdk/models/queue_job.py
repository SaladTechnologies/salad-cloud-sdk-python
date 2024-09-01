from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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

    :param id_: id_
    :type id_: str
    :param input: The job input. May be any valid JSON.
    :type input: any
    :param metadata: metadata, defaults to None
    :type metadata: dict, optional
    :param webhook: webhook, defaults to None
    :type webhook: str, optional
    :param status: status
    :type status: QueueJobStatus
    :param events: events
    :type events: List[QueueJobEvent]
    :param output: The job output. May be any valid JSON., defaults to None
    :type output: any, optional
    :param create_time: create_time
    :type create_time: str
    :param update_time: update_time
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
        metadata: dict = None,
        webhook: str = None,
        output: any = None,
    ):
        """Represents a queue job

        :param id_: id_
        :type id_: str
        :param input: The job input. May be any valid JSON.
        :type input: any
        :param metadata: metadata, defaults to None
        :type metadata: dict, optional
        :param webhook: webhook, defaults to None
        :type webhook: str, optional
        :param status: status
        :type status: QueueJobStatus
        :param events: events
        :type events: List[QueueJobEvent]
        :param output: The job output. May be any valid JSON., defaults to None
        :type output: any, optional
        :param create_time: create_time
        :type create_time: str
        :param update_time: update_time
        :type update_time: str
        """
        self.id_ = id_
        self.input = input
        self.metadata = metadata
        self.webhook = self._define_str("webhook", webhook, nullable=True)
        self.status = self._enum_matching(status, QueueJobStatus.list(), "status")
        self.events = self._define_list(events, QueueJobEvent)
        self.output = output
        self.create_time = create_time
        self.update_time = update_time
