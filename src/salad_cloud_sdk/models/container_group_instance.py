from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .the_container_group_instance_state import TheContainerGroupInstanceState


@JsonMap({"id_": "id"})
class ContainerGroupInstance(BaseModel):
    """A Container Group Instance represents a running instance of a container group on a specific machine. It provides information about the execution state, readiness, and version of the deployed container group.

    :param id_: The container group instance identifier.
    :type id_: str
    :param machine_id: The container group machine identifier.
    :type machine_id: str
    :param ssh_ip: The SSH IP address of the container group instance, defaults to None
    :type ssh_ip: str, optional
    :param ssh_port: The SSH port of the container group instance, defaults to None
    :type ssh_port: int, optional
    :param ssh_host_key_fingerprint: The SSH host key fingerprint of the container group instance, defaults to None
    :type ssh_host_key_fingerprint: str, optional
    :param state: The state of the container group instance
    :type state: TheContainerGroupInstanceState
    :param update_time: The UTC timestamp when the container group instance last changed its state. This helps track the lifecycle and state transitions of the instance.
    :type update_time: str
    :param version: The version of the container group definition currently running on this instance. Used to track deployment and update progress across the container group fleet.
    :type version: int
    :param ready: Indicates whether the container group instance is currently passing its readiness checks and is able to receive traffic or perform its intended function. If no readiness probe is defined, this will be true once the instance is fully started., defaults to None
    :type ready: bool, optional
    :param started: Indicates whether the container group instance has successfully completed its startup sequence and passed any configured startup probes. This will always be true when no startup probe is defined for the container group., defaults to None
    :type started: bool, optional
    :param deletion_cost: The cost of deleting the container group instance, defaults to None
    :type deletion_cost: int, optional
    """

    def __init__(
        self,
        id_: str,
        machine_id: str,
        state: TheContainerGroupInstanceState,
        update_time: str,
        version: int,
        ssh_ip: str = SENTINEL,
        ssh_port: int = SENTINEL,
        ssh_host_key_fingerprint: str = SENTINEL,
        ready: bool = SENTINEL,
        started: bool = SENTINEL,
        deletion_cost: int = SENTINEL,
        **kwargs,
    ):
        """A Container Group Instance represents a running instance of a container group on a specific machine. It provides information about the execution state, readiness, and version of the deployed container group.

        :param id_: The container group instance identifier.
        :type id_: str
        :param machine_id: The container group machine identifier.
        :type machine_id: str
        :param ssh_ip: The SSH IP address of the container group instance, defaults to None
        :type ssh_ip: str, optional
        :param ssh_port: The SSH port of the container group instance, defaults to None
        :type ssh_port: int, optional
        :param ssh_host_key_fingerprint: The SSH host key fingerprint of the container group instance, defaults to None
        :type ssh_host_key_fingerprint: str, optional
        :param state: The state of the container group instance
        :type state: TheContainerGroupInstanceState
        :param update_time: The UTC timestamp when the container group instance last changed its state. This helps track the lifecycle and state transitions of the instance.
        :type update_time: str
        :param version: The version of the container group definition currently running on this instance. Used to track deployment and update progress across the container group fleet.
        :type version: int
        :param ready: Indicates whether the container group instance is currently passing its readiness checks and is able to receive traffic or perform its intended function. If no readiness probe is defined, this will be true once the instance is fully started., defaults to None
        :type ready: bool, optional
        :param started: Indicates whether the container group instance has successfully completed its startup sequence and passed any configured startup probes. This will always be true when no startup probe is defined for the container group., defaults to None
        :type started: bool, optional
        :param deletion_cost: The cost of deleting the container group instance, defaults to None
        :type deletion_cost: int, optional
        """
        self.id_ = id_
        self.machine_id = machine_id
        if ssh_ip is not SENTINEL:
            self.ssh_ip = ssh_ip
        if ssh_port is not SENTINEL:
            self.ssh_port = self._define_number("ssh_port", ssh_port, ge=1, le=65535)
        if ssh_host_key_fingerprint is not SENTINEL:
            self.ssh_host_key_fingerprint = self._define_str(
                "ssh_host_key_fingerprint",
                ssh_host_key_fingerprint,
                min_length=1,
                max_length=256,
            )
        self.state = self._enum_matching(
            state, TheContainerGroupInstanceState.list(), "state"
        )
        self.update_time = update_time
        self.version = self._define_number("version", version, ge=1, le=2147483647)
        if ready is not SENTINEL:
            self.ready = ready
        if started is not SENTINEL:
            self.started = started
        if deletion_cost is not SENTINEL:
            self.deletion_cost = self._define_number(
                "deletion_cost", deletion_cost, ge=0, le=100000
            )
        self._kwargs = kwargs
