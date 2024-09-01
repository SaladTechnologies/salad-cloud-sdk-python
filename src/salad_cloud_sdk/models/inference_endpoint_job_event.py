from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class InferenceEndpointJobEventAction(Enum):
    """An enumeration representing different categories.

    :cvar CREATED: "created"
    :vartype CREATED: str
    :cvar STARTED: "started"
    :vartype STARTED: str
    :cvar SUCCEEDED: "succeeded"
    :vartype SUCCEEDED: str
    :cvar CANCELLED: "cancelled"
    :vartype CANCELLED: str
    :cvar FAILED: "failed"
    :vartype FAILED: str
    """

    CREATED = "created"
    STARTED = "started"
    SUCCEEDED = "succeeded"
    CANCELLED = "cancelled"
    FAILED = "failed"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, InferenceEndpointJobEventAction._member_map_.values()
            )
        )


@JsonMap({})
class InferenceEndpointJobEvent(BaseModel):
    """Represents an event for inference endpoint job

    :param action: action
    :type action: InferenceEndpointJobEventAction
    :param time: time
    :type time: str
    """

    def __init__(self, action: InferenceEndpointJobEventAction, time: str):
        """Represents an event for inference endpoint job

        :param action: action
        :type action: InferenceEndpointJobEventAction
        :param time: time
        :type time: str
        """
        self.action = self._enum_matching(
            action, InferenceEndpointJobEventAction.list(), "action"
        )
        self.time = time
