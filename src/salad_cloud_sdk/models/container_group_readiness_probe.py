from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group_probe_tcp import ContainerGroupProbeTcp
from .container_group_probe_http import ContainerGroupProbeHttp
from .container_group_probe_grpc import ContainerGroupProbeGrpc
from .container_group_probe_exec import ContainerGroupProbeExec


@JsonMap({"exec_": "exec"})
class ContainerGroupReadinessProbe(BaseModel):
    """Represents the container group readiness probe

    :param tcp: tcp, defaults to None
    :type tcp: ContainerGroupProbeTcp, optional
    :param http: http, defaults to None
    :type http: ContainerGroupProbeHttp, optional
    :param grpc: grpc, defaults to None
    :type grpc: ContainerGroupProbeGrpc, optional
    :param exec_: exec_, defaults to None
    :type exec_: ContainerGroupProbeExec, optional
    :param initial_delay_seconds: initial_delay_seconds
    :type initial_delay_seconds: int
    :param period_seconds: period_seconds
    :type period_seconds: int
    :param timeout_seconds: timeout_seconds
    :type timeout_seconds: int
    :param success_threshold: success_threshold
    :type success_threshold: int
    :param failure_threshold: failure_threshold
    :type failure_threshold: int
    """

    def __init__(
        self,
        initial_delay_seconds: int,
        period_seconds: int,
        timeout_seconds: int,
        success_threshold: int,
        failure_threshold: int,
        tcp: ContainerGroupProbeTcp = None,
        http: ContainerGroupProbeHttp = None,
        grpc: ContainerGroupProbeGrpc = None,
        exec_: ContainerGroupProbeExec = None,
    ):
        """Represents the container group readiness probe

        :param tcp: tcp, defaults to None
        :type tcp: ContainerGroupProbeTcp, optional
        :param http: http, defaults to None
        :type http: ContainerGroupProbeHttp, optional
        :param grpc: grpc, defaults to None
        :type grpc: ContainerGroupProbeGrpc, optional
        :param exec_: exec_, defaults to None
        :type exec_: ContainerGroupProbeExec, optional
        :param initial_delay_seconds: initial_delay_seconds
        :type initial_delay_seconds: int
        :param period_seconds: period_seconds
        :type period_seconds: int
        :param timeout_seconds: timeout_seconds
        :type timeout_seconds: int
        :param success_threshold: success_threshold
        :type success_threshold: int
        :param failure_threshold: failure_threshold
        :type failure_threshold: int
        """
        self.tcp = self._define_object(tcp, ContainerGroupProbeTcp)
        self.http = self._define_object(http, ContainerGroupProbeHttp)
        self.grpc = self._define_object(grpc, ContainerGroupProbeGrpc)
        self.exec_ = self._define_object(exec_, ContainerGroupProbeExec)
        self.initial_delay_seconds = self._define_number(
            "initial_delay_seconds", initial_delay_seconds, ge=0
        )
        self.period_seconds = self._define_number(
            "period_seconds", period_seconds, ge=1
        )
        self.timeout_seconds = self._define_number(
            "timeout_seconds", timeout_seconds, ge=1
        )
        self.success_threshold = self._define_number(
            "success_threshold", success_threshold, ge=1
        )
        self.failure_threshold = self._define_number(
            "failure_threshold", failure_threshold, ge=1
        )
