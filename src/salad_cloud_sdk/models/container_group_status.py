from enum import Enum


class ContainerGroupStatus(Enum):
    """An enumeration representing different categories.

    :cvar PENDING: "pending"
    :vartype PENDING: str
    :cvar RUNNING: "running"
    :vartype RUNNING: str
    :cvar STOPPED: "stopped"
    :vartype STOPPED: str
    :cvar SUCCEEDED: "succeeded"
    :vartype SUCCEEDED: str
    :cvar FAILED: "failed"
    :vartype FAILED: str
    :cvar DEPLOYING: "deploying"
    :vartype DEPLOYING: str
    """

    PENDING = "pending"
    RUNNING = "running"
    STOPPED = "stopped"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    DEPLOYING = "deploying"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ContainerGroupStatus._member_map_.values()))
