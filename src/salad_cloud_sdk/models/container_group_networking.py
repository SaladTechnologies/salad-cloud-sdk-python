from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_networking_protocol import ContainerNetworkingProtocol


@JsonMap({})
class ContainerGroupNetworking(BaseModel):
    """Represents container group networking parameters

    :param protocol: protocol
    :type protocol: ContainerNetworkingProtocol
    :param port: port
    :type port: int
    :param auth: auth
    :type auth: bool
    :param dns: dns
    :type dns: str
    """

    def __init__(
        self, protocol: ContainerNetworkingProtocol, port: int, auth: bool, dns: str
    ):
        """Represents container group networking parameters

        :param protocol: protocol
        :type protocol: ContainerNetworkingProtocol
        :param port: port
        :type port: int
        :param auth: auth
        :type auth: bool
        :param dns: dns
        :type dns: str
        """
        self.protocol = self._enum_matching(
            protocol, ContainerNetworkingProtocol.list(), "protocol"
        )
        self.port = self._define_number("port", port, ge=1, le=65535)
        self.auth = auth
        self.dns = dns
