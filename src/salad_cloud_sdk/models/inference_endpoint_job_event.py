from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inference_endpoint_job_event_action import InferenceEndpointJobEventAction


@JsonMap({})
class InferenceEndpointJobEvent(BaseModel):
    """Represents an event for inference endpoint job

    :param action: The action that was taken on the inference endpoint job.
    :type action: InferenceEndpointJobEventAction
    :param time: The time the event occurred.
    :type time: str
    """

    def __init__(self, action: InferenceEndpointJobEventAction, time: str, **kwargs):
        """Represents an event for inference endpoint job

        :param action: The action that was taken on the inference endpoint job.
        :type action: InferenceEndpointJobEventAction
        :param time: The time the event occurred.
        :type time: str
        """
        self.action = self._enum_matching(
            action, InferenceEndpointJobEventAction.list(), "action"
        )
        self.time = time
        self._kwargs = kwargs
