from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class QueueJobEventAction(Enum):
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
        return list(map(lambda x: x.value, QueueJobEventAction._member_map_.values()))


@JsonMap({})
class QueueJobEvent(BaseModel):
    """Represents an event for queue job

    :param action: action
    :type action: QueueJobEventAction
    :param time: time
    :type time: str
    """

    def __init__(self, action: QueueJobEventAction, time: str):
        """Represents an event for queue job

        :param action: action
        :type action: QueueJobEventAction
        :param time: time
        :type time: str
        """
        self.action = self._enum_matching(action, QueueJobEventAction.list(), "action")
        self.time = time
