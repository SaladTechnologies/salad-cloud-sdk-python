from enum import Enum


class TheContainerGroupInstanceState(Enum):
    """An enumeration representing different categories.

    :cvar ALLOCATING: "allocating"
    :vartype ALLOCATING: str
    :cvar DOWNLOADING: "downloading"
    :vartype DOWNLOADING: str
    :cvar CREATING: "creating"
    :vartype CREATING: str
    :cvar RUNNING: "running"
    :vartype RUNNING: str
    :cvar STOPPING: "stopping"
    :vartype STOPPING: str
    """

    ALLOCATING = "allocating"
    DOWNLOADING = "downloading"
    CREATING = "creating"
    RUNNING = "running"
    STOPPING = "stopping"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, TheContainerGroupInstanceState._member_map_.values())
        )
