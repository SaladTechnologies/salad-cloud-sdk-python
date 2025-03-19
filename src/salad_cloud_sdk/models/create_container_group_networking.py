from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .the_container_group_networking_load_balancer import (
    TheContainerGroupNetworkingLoadBalancer,
)
from .container_networking_protocol import ContainerNetworkingProtocol


@JsonMap({})
class CreateContainerGroupNetworking(BaseModel):
    """Network configuration for container groups specifying connectivity parameters, including authentication, protocol, and timeout settings

    :param auth: Determines whether authentication is required for network connections to the container group
    :type auth: bool
    :param client_request_timeout: The container group networking client request timeout., defaults to None
    :type client_request_timeout: int, optional
    :param load_balancer: The container group networking load balancer., defaults to None
    :type load_balancer: TheContainerGroupNetworkingLoadBalancer, optional
    :param port: The container group networking port.
    :type port: int
    :param protocol: Defines the communication protocol used for network traffic between containers or external systems. Currently supports HTTP protocol for web-based communication.
    :type protocol: ContainerNetworkingProtocol
    :param server_response_timeout: The container group networking server response timeout., defaults to None
    :type server_response_timeout: int, optional
    :param single_connection_limit: The container group networking single connection limit flag., defaults to None
    :type single_connection_limit: bool, optional
    """

    def __init__(
        self,
        auth: bool,
        port: int,
        protocol: ContainerNetworkingProtocol,
        client_request_timeout: int = SENTINEL,
        load_balancer: TheContainerGroupNetworkingLoadBalancer = SENTINEL,
        server_response_timeout: int = SENTINEL,
        single_connection_limit: bool = SENTINEL,
        **kwargs,
    ):
        """Network configuration for container groups specifying connectivity parameters, including authentication, protocol, and timeout settings

        :param auth: Determines whether authentication is required for network connections to the container group
        :type auth: bool
        :param client_request_timeout: The container group networking client request timeout., defaults to None
        :type client_request_timeout: int, optional
        :param load_balancer: The container group networking load balancer., defaults to None
        :type load_balancer: TheContainerGroupNetworkingLoadBalancer, optional
        :param port: The container group networking port.
        :type port: int
        :param protocol: Defines the communication protocol used for network traffic between containers or external systems. Currently supports HTTP protocol for web-based communication.
        :type protocol: ContainerNetworkingProtocol
        :param server_response_timeout: The container group networking server response timeout., defaults to None
        :type server_response_timeout: int, optional
        :param single_connection_limit: The container group networking single connection limit flag., defaults to None
        :type single_connection_limit: bool, optional
        """
        self.auth = auth
        if client_request_timeout is not SENTINEL:
            self.client_request_timeout = self._define_number(
                "client_request_timeout", client_request_timeout, ge=1, le=100000
            )
        if load_balancer is not SENTINEL:
            self.load_balancer = self._enum_matching(
                load_balancer,
                TheContainerGroupNetworkingLoadBalancer.list(),
                "load_balancer",
            )
        self.port = self._define_number("port", port, ge=1, le=65535)
        self.protocol = self._enum_matching(
            protocol, ContainerNetworkingProtocol.list(), "protocol"
        )
        if server_response_timeout is not SENTINEL:
            self.server_response_timeout = self._define_number(
                "server_response_timeout", server_response_timeout, ge=1, le=100000
            )
        if single_connection_limit is not SENTINEL:
            self.single_connection_limit = single_connection_limit
        self._kwargs = kwargs
