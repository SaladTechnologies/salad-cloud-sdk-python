from enum import Enum


class TheContainerGroupNetworkingLoadBalancer(Enum):
    """An enumeration representing different categories.

    :cvar ROUNDROBIN: "round_robin"
    :vartype ROUNDROBIN: str
    :cvar LEASTNUMBEROFCONNECTIONS: "least_number_of_connections"
    :vartype LEASTNUMBEROFCONNECTIONS: str
    """

    ROUNDROBIN = "round_robin"
    LEASTNUMBEROFCONNECTIONS = "least_number_of_connections"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                TheContainerGroupNetworkingLoadBalancer._member_map_.values(),
            )
        )
