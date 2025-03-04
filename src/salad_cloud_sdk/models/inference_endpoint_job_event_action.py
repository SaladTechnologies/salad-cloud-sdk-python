from enum import Enum


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
