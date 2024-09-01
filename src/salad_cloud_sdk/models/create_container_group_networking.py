from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_networking_protocol import ContainerNetworkingProtocol


@JsonMap({})
class CreateContainerGroupNetworking(BaseModel):
    """Represents container group networking parameters

    :param protocol: protocol
    :type protocol: ContainerNetworkingProtocol
    :param port: port
    :type port: int
    :param auth: auth
    :type auth: bool
    """

    def __init__(self, protocol: ContainerNetworkingProtocol, port: int, auth: bool):
        """Represents container group networking parameters

        :param protocol: protocol
        :type protocol: ContainerNetworkingProtocol
        :param port: port
        :type port: int
        :param auth: auth
        :type auth: bool
        """
        self.protocol = self._enum_matching(
            protocol, ContainerNetworkingProtocol.list(), "protocol"
        )
        self.port = self._define_number("port", port, ge=1, le=65535)
        self.auth = auth
