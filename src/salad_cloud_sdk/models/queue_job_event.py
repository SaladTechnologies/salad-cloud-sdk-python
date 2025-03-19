from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class Action(Enum):
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
        return list(map(lambda x: x.value, Action._member_map_.values()))


@JsonMap({})
class QueueJobEvent(BaseModel):
    """Represents an event for queue job

    :param action: The action that was taken on the queue job
    :type action: Action
    :param time: The time the action was taken on the queue job
    :type time: str
    """

    def __init__(self, action: Action, time: str, **kwargs):
        """Represents an event for queue job

        :param action: The action that was taken on the queue job
        :type action: Action
        :param time: The time the action was taken on the queue job
        :type time: str
        """
        self.action = self._enum_matching(action, Action.list(), "action")
        self.time = time
        self._kwargs = kwargs
