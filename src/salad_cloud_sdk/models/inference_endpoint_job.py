from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inference_endpoint_job_event import InferenceEndpointJobEvent


class InferenceEndpointJobStatus(Enum):
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
        return list(
            map(lambda x: x.value, InferenceEndpointJobStatus._member_map_.values())
        )


@JsonMap({"id_": "id"})
class InferenceEndpointJob(BaseModel):
    """Represents a inference endpoint job

    :param id_: id_
    :type id_: str
    :param input: The job input. May be any valid JSON.
    :type input: any
    :param inference_endpoint_name: The inference endpoint name
    :type inference_endpoint_name: str
    :param metadata: metadata, defaults to None
    :type metadata: dict, optional
    :param webhook: webhook, defaults to None
    :type webhook: str, optional
    :param status: status
    :type status: InferenceEndpointJobStatus
    :param events: events
    :type events: List[InferenceEndpointJobEvent]
    :param organization_name: The organization name
    :type organization_name: str
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
        inference_endpoint_name: str,
        status: InferenceEndpointJobStatus,
        events: List[InferenceEndpointJobEvent],
        organization_name: str,
        create_time: str,
        update_time: str,
        metadata: dict = None,
        webhook: str = None,
        output: any = None,
    ):
        """Represents a inference endpoint job

        :param id_: id_
        :type id_: str
        :param input: The job input. May be any valid JSON.
        :type input: any
        :param inference_endpoint_name: The inference endpoint name
        :type inference_endpoint_name: str
        :param metadata: metadata, defaults to None
        :type metadata: dict, optional
        :param webhook: webhook, defaults to None
        :type webhook: str, optional
        :param status: status
        :type status: InferenceEndpointJobStatus
        :param events: events
        :type events: List[InferenceEndpointJobEvent]
        :param organization_name: The organization name
        :type organization_name: str
        :param output: The job output. May be any valid JSON., defaults to None
        :type output: any, optional
        :param create_time: create_time
        :type create_time: str
        :param update_time: update_time
        :type update_time: str
        """
        self.id_ = id_
        self.input = input
        self.inference_endpoint_name = inference_endpoint_name
        self.metadata = metadata
        self.webhook = self._define_str("webhook", webhook, nullable=True)
        self.status = self._enum_matching(
            status, InferenceEndpointJobStatus.list(), "status"
        )
        self.events = self._define_list(events, InferenceEndpointJobEvent)
        self.organization_name = organization_name
        self.output = output
        self.create_time = create_time
        self.update_time = update_time
