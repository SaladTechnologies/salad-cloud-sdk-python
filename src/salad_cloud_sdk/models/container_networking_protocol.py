from enum import Enum


class ContainerNetworkingProtocol(Enum):
    """An enumeration representing different categories.

    :cvar HTTP: "http"
    :vartype HTTP: str
    """

    HTTP = "http"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ContainerNetworkingProtocol._member_map_.values())
        )
