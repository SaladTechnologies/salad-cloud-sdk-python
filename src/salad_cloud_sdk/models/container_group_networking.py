from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_networking_protocol import ContainerNetworkingProtocol


class ContainerGroupNetworkingLoadBalancer(Enum):
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
                ContainerGroupNetworkingLoadBalancer._member_map_.values(),
            )
        )


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
    :param load_balancer: load_balancer, defaults to None
    :type load_balancer: ContainerGroupNetworkingLoadBalancer, optional
    :param single_connection_limit: single_connection_limit, defaults to None
    :type single_connection_limit: bool, optional
    :param client_request_timeout: client_request_timeout, defaults to None
    :type client_request_timeout: int, optional
    :param server_response_timeout: server_response_timeout, defaults to None
    :type server_response_timeout: int, optional
    """

    def __init__(
        self,
        protocol: ContainerNetworkingProtocol,
        port: int,
        auth: bool,
        dns: str,
        load_balancer: ContainerGroupNetworkingLoadBalancer = None,
        single_connection_limit: bool = None,
        client_request_timeout: int = None,
        server_response_timeout: int = None,
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
        :param load_balancer: load_balancer, defaults to None
        :type load_balancer: ContainerGroupNetworkingLoadBalancer, optional
        :param single_connection_limit: single_connection_limit, defaults to None
        :type single_connection_limit: bool, optional
        :param client_request_timeout: client_request_timeout, defaults to None
        :type client_request_timeout: int, optional
        :param server_response_timeout: server_response_timeout, defaults to None
        :type server_response_timeout: int, optional
        """
        self.protocol = self._enum_matching(
            protocol, ContainerNetworkingProtocol.list(), "protocol"
        )
        self.port = self._define_number("port", port, ge=1, le=65535)
        self.auth = auth
        self.dns = dns
        if load_balancer is not None:
            self.load_balancer = self._enum_matching(
                load_balancer,
                ContainerGroupNetworkingLoadBalancer.list(),
                "load_balancer",
            )
        if single_connection_limit is not None:
            self.single_connection_limit = single_connection_limit
        if client_request_timeout is not None:
            self.client_request_timeout = self._define_number(
                "client_request_timeout", client_request_timeout, ge=1, le=100000
            )
        if server_response_timeout is not None:
            self.server_response_timeout = self._define_number(
                "server_response_timeout", server_response_timeout, ge=1, le=100000
            )
