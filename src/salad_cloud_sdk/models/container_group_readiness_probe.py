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
class ContainerGroupReadinessProbe(BaseModel):
    """Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it.

    :param exec_: Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks., defaults to None
    :type exec_: ContainerGroupProbeExec, optional
    :param failure_threshold: The number of consecutive failures required to consider the probe failed. After this many consecutive failures, the container is marked as not ready.
    :type failure_threshold: int
    :param grpc: Configuration for gRPC-based health probes in container groups, used to determine container health status., defaults to None
    :type grpc: ContainerGroupGRpcProbe, optional
    :param http: Defines HTTP probe configuration for container health checks within a container group., defaults to None
    :type http: ContainerGroupHttpProbeConfiguration, optional
    :param initial_delay_seconds: The time in seconds to wait after the container starts before initiating the first probe. This allows time for the application to initialize before being tested.
    :type initial_delay_seconds: int
    :param period_seconds: How frequently (in seconds) the probe should be executed during the container's lifetime. Specifies the interval between consecutive probe executions.
    :type period_seconds: int
    :param success_threshold: The minimum consecutive successes required to consider the probe successful after it has failed. Defines how many successful probe results are needed to transition from failure to success.
    :type success_threshold: int
    :param tcp: Configuration for a TCP probe used to check container health via network connectivity., defaults to None
    :type tcp: ContainerGroupTcpProbe, optional
    :param timeout_seconds: The maximum time in seconds that the probe has to complete. If the probe doesn't return a result before the timeout, it's considered failed.
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
        """Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it.

        :param exec_: Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks., defaults to None
        :type exec_: ContainerGroupProbeExec, optional
        :param failure_threshold: The number of consecutive failures required to consider the probe failed. After this many consecutive failures, the container is marked as not ready.
        :type failure_threshold: int
        :param grpc: Configuration for gRPC-based health probes in container groups, used to determine container health status., defaults to None
        :type grpc: ContainerGroupGRpcProbe, optional
        :param http: Defines HTTP probe configuration for container health checks within a container group., defaults to None
        :type http: ContainerGroupHttpProbeConfiguration, optional
        :param initial_delay_seconds: The time in seconds to wait after the container starts before initiating the first probe. This allows time for the application to initialize before being tested.
        :type initial_delay_seconds: int
        :param period_seconds: How frequently (in seconds) the probe should be executed during the container's lifetime. Specifies the interval between consecutive probe executions.
        :type period_seconds: int
        :param success_threshold: The minimum consecutive successes required to consider the probe successful after it has failed. Defines how many successful probe results are needed to transition from failure to success.
        :type success_threshold: int
        :param tcp: Configuration for a TCP probe used to check container health via network connectivity., defaults to None
        :type tcp: ContainerGroupTcpProbe, optional
        :param timeout_seconds: The maximum time in seconds that the probe has to complete. If the probe doesn't return a result before the timeout, it's considered failed.
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
