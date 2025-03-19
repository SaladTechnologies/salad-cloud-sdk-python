from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .status import Status
from .inference_endpoint_job_event import InferenceEndpointJobEvent


@JsonMap({"id_": "id"})
class InferenceEndpointJob(BaseModel):
    """Represents a inference endpoint job

    :param id_: The inference endpoint job identifier.
    :type id_: str
    :param inference_endpoint_name: The inference endpoint name.
    :type inference_endpoint_name: str
    :param organization_name: The organization name.
    :type organization_name: str
    :param input: The job input. May be any valid JSON.
    :type input: any
    :param metadata: The job metadata. May be any valid JSON., defaults to None
    :type metadata: dict, optional
    :param webhook: The webhook URL called when the job completes., defaults to None
    :type webhook: str, optional
    :param webhook_url: The webhook URL called when the job completes., defaults to None
    :type webhook_url: str, optional
    :param status: The current status.
    :type status: Status
    :param events: The list of events.
    :type events: List[InferenceEndpointJobEvent]
    :param output: The job output. May be any valid JSON., defaults to None
    :type output: any, optional
    :param create_time: The time the job was created.
    :type create_time: str
    :param update_time: The time the job was last updated.
    :type update_time: str
    """

    def __init__(
        self,
        id_: str,
        inference_endpoint_name: str,
        organization_name: str,
        input: any,
        status: Status,
        events: List[InferenceEndpointJobEvent],
        create_time: str,
        update_time: str,
        metadata: dict = SENTINEL,
        webhook: str = SENTINEL,
        webhook_url: str = SENTINEL,
        output: any = SENTINEL,
        **kwargs,
    ):
        """Represents a inference endpoint job

        :param id_: The inference endpoint job identifier.
        :type id_: str
        :param inference_endpoint_name: The inference endpoint name.
        :type inference_endpoint_name: str
        :param organization_name: The organization name.
        :type organization_name: str
        :param input: The job input. May be any valid JSON.
        :type input: any
        :param metadata: The job metadata. May be any valid JSON., defaults to None
        :type metadata: dict, optional
        :param webhook: The webhook URL called when the job completes., defaults to None
        :type webhook: str, optional
        :param webhook_url: The webhook URL called when the job completes., defaults to None
        :type webhook_url: str, optional
        :param status: The current status.
        :type status: Status
        :param events: The list of events.
        :type events: List[InferenceEndpointJobEvent]
        :param output: The job output. May be any valid JSON., defaults to None
        :type output: any, optional
        :param create_time: The time the job was created.
        :type create_time: str
        :param update_time: The time the job was last updated.
        :type update_time: str
        """
        self.id_ = id_
        self.inference_endpoint_name = self._define_str(
            "inference_endpoint_name",
            inference_endpoint_name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.organization_name = self._define_str(
            "organization_name",
            organization_name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.input = input
        if metadata is not SENTINEL:
            self.metadata = metadata
        if webhook is not SENTINEL:
            self.webhook = self._define_str(
                "webhook", webhook, min_length=1, max_length=2048
            )
        if webhook_url is not SENTINEL:
            self.webhook_url = self._define_str(
                "webhook_url", webhook_url, min_length=1, max_length=2048
            )
        self.status = self._enum_matching(status, Status.list(), "status")
        self.events = self._define_list(events, InferenceEndpointJobEvent)
        if output is not SENTINEL:
            self.output = output
        self.create_time = create_time
        self.update_time = update_time
        self._kwargs = kwargs
