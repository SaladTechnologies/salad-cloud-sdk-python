from enum import Enum


class ContainerGroupPriority(Enum):
    """An enumeration representing different categories.

    :cvar HIGH: "high"
    :vartype HIGH: str
    :cvar MEDIUM: "medium"
    :vartype MEDIUM: str
    :cvar LOW: "low"
    :vartype LOW: str
    :cvar BATCH: "batch"
    :vartype BATCH: str
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    BATCH = "batch"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ContainerGroupPriority._member_map_.values())
        )
