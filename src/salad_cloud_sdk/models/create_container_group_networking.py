from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_networking_protocol import ContainerNetworkingProtocol


class CreateContainerGroupNetworkingLoadBalancer(Enum):
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
                CreateContainerGroupNetworkingLoadBalancer._member_map_.values(),
            )
        )


@JsonMap({})
class CreateContainerGroupNetworking(BaseModel):
    """Represents container group networking parameters

    :param protocol: protocol
    :type protocol: ContainerNetworkingProtocol
    :param port: port
    :type port: int
    :param auth: auth
    :type auth: bool
    :param load_balancer: load_balancer, defaults to None
    :type load_balancer: CreateContainerGroupNetworkingLoadBalancer, optional
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
        load_balancer: CreateContainerGroupNetworkingLoadBalancer = SENTINEL,
        single_connection_limit: bool = SENTINEL,
        client_request_timeout: int = SENTINEL,
        server_response_timeout: int = SENTINEL,
        **kwargs,
    ):
        """Represents container group networking parameters

        :param protocol: protocol
        :type protocol: ContainerNetworkingProtocol
        :param port: port
        :type port: int
        :param auth: auth
        :type auth: bool
        :param load_balancer: load_balancer, defaults to None
        :type load_balancer: CreateContainerGroupNetworkingLoadBalancer, optional
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
        if load_balancer is not SENTINEL:
            self.load_balancer = self._enum_matching(
                load_balancer,
                CreateContainerGroupNetworkingLoadBalancer.list(),
                "load_balancer",
            )
        if single_connection_limit is not SENTINEL:
            self.single_connection_limit = single_connection_limit
        if client_request_timeout is not SENTINEL:
            self.client_request_timeout = self._define_number(
                "client_request_timeout", client_request_timeout, ge=1, le=100000
            )
        if server_response_timeout is not SENTINEL:
            self.server_response_timeout = self._define_number(
                "server_response_timeout", server_response_timeout, ge=1, le=100000
            )
        self._kwargs = kwargs
