from __future__ import annotations
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_group_probe_exec import ContainerGroupProbeExec
from .container_group_g_rpc_probe import ContainerGroupGRpcProbe
from .container_group_http_probe_configuration import (
    ContainerGroupHttpProbeConfiguration,
)
from .container_group_tcp_probe import ContainerGroupTcpProbe


@JsonMap({"exec_": "exec"})
class ContainerGroupLivenessProbe(BaseModel):
    """Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy

    :param exec_: Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks., defaults to None
    :type exec_: ContainerGroupProbeExec, optional
    :param failure_threshold: Number of consecutive failures required to consider the probe as failed
    :type failure_threshold: int
    :param grpc: Configuration for gRPC-based health probes in container groups, used to determine container health status., defaults to None
    :type grpc: ContainerGroupGRpcProbe, optional
    :param http: Defines HTTP probe configuration for container health checks within a container group., defaults to None
    :type http: ContainerGroupHttpProbeConfiguration, optional
    :param initial_delay_seconds: Number of seconds to wait after container start before initiating liveness probes
    :type initial_delay_seconds: int
    :param period_seconds: Frequency in seconds at which the probe should be executed
    :type period_seconds: int
    :param success_threshold: Number of consecutive successes required to consider the probe successful
    :type success_threshold: int
    :param tcp: Configuration for a TCP probe used to check container health via network connectivity., defaults to None
    :type tcp: ContainerGroupTcpProbe, optional
    :param timeout_seconds: Number of seconds after which the probe times out if no response is received
    :type timeout_seconds: int
    """

    def __init__(
        self,
        failure_threshold: int,
        initial_delay_seconds: int,
        period_seconds: int,
        success_threshold: int,
        timeout_seconds: int,
        exec_: ContainerGroupProbeExec = SENTINEL,
        grpc: ContainerGroupGRpcProbe = SENTINEL,
        http: ContainerGroupHttpProbeConfiguration = SENTINEL,
        tcp: ContainerGroupTcpProbe = SENTINEL,
        **kwargs,
    ):
        """Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy

        :param exec_: Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks., defaults to None
        :type exec_: ContainerGroupProbeExec, optional
        :param failure_threshold: Number of consecutive failures required to consider the probe as failed
        :type failure_threshold: int
        :param grpc: Configuration for gRPC-based health probes in container groups, used to determine container health status., defaults to None
        :type grpc: ContainerGroupGRpcProbe, optional
        :param http: Defines HTTP probe configuration for container health checks within a container group., defaults to None
        :type http: ContainerGroupHttpProbeConfiguration, optional
        :param initial_delay_seconds: Number of seconds to wait after container start before initiating liveness probes
        :type initial_delay_seconds: int
        :param period_seconds: Frequency in seconds at which the probe should be executed
        :type period_seconds: int
        :param success_threshold: Number of consecutive successes required to consider the probe successful
        :type success_threshold: int
        :param tcp: Configuration for a TCP probe used to check container health via network connectivity., defaults to None
        :type tcp: ContainerGroupTcpProbe, optional
        :param timeout_seconds: Number of seconds after which the probe times out if no response is received
        :type timeout_seconds: int
        """
        if exec_ is not SENTINEL:
            self.exec_ = self._define_object(exec_, ContainerGroupProbeExec)
        self.failure_threshold = self._define_number(
            "failure_threshold", failure_threshold, ge=1, le=20
        )
        if grpc is not SENTINEL:
            self.grpc = self._define_object(grpc, ContainerGroupGRpcProbe)
        if http is not SENTINEL:
            self.http = self._define_object(http, ContainerGroupHttpProbeConfiguration)
        self.initial_delay_seconds = self._define_number(
            "initial_delay_seconds", initial_delay_seconds, ge=0, le=1200
        )
        self.period_seconds = self._define_number(
            "period_seconds", period_seconds, ge=1, le=120
        )
        self.success_threshold = self._define_number(
            "success_threshold", success_threshold, ge=1, le=10
        )
        if tcp is not SENTINEL:
            self.tcp = self._define_object(tcp, ContainerGroupTcpProbe)
        self.timeout_seconds = self._define_number(
            "timeout_seconds", timeout_seconds, ge=1, le=60
        )
        self._kwargs = kwargs
