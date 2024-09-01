from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container import Container
from .container_restart_policy import ContainerRestartPolicy
from .container_group_state import ContainerGroupState
from .country_code import CountryCode
from .container_group_networking import ContainerGroupNetworking
from .container_group_liveness_probe import ContainerGroupLivenessProbe
from .container_group_readiness_probe import ContainerGroupReadinessProbe
from .container_group_startup_probe import ContainerGroupStartupProbe
from .container_group_queue_connection import ContainerGroupQueueConnection


@JsonMap({"id_": "id"})
class ContainerGroup(BaseModel):
    """Represents a container group

    :param id_: id_
    :type id_: str
    :param name: name
    :type name: str
    :param display_name: display_name
    :type display_name: str
    :param container: Represents a container
    :type container: Container
    :param autostart_policy: autostart_policy
    :type autostart_policy: bool
    :param restart_policy: restart_policy
    :type restart_policy: ContainerRestartPolicy
    :param replicas: replicas
    :type replicas: int
    :param current_state: Represents a container group state
    :type current_state: ContainerGroupState
    :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
    :type country_codes: List[CountryCode], optional
    :param networking: Represents container group networking parameters, defaults to None
    :type networking: ContainerGroupNetworking, optional
    :param liveness_probe: Represents the container group liveness probe, defaults to None
    :type liveness_probe: ContainerGroupLivenessProbe, optional
    :param readiness_probe: Represents the container group readiness probe, defaults to None
    :type readiness_probe: ContainerGroupReadinessProbe, optional
    :param startup_probe: Represents the container group startup probe, defaults to None
    :type startup_probe: ContainerGroupStartupProbe, optional
    :param queue_connection: Represents container group queue connection, defaults to None
    :type queue_connection: ContainerGroupQueueConnection, optional
    :param create_time: create_time
    :type create_time: str
    :param update_time: update_time
    :type update_time: str
    :param pending_change: pending_change
    :type pending_change: bool
    :param version: version
    :type version: int
    """

    def __init__(
        self,
        id_: str,
        name: str,
        display_name: str,
        container: Container,
        autostart_policy: bool,
        restart_policy: ContainerRestartPolicy,
        replicas: int,
        current_state: ContainerGroupState,
        create_time: str,
        update_time: str,
        pending_change: bool,
        version: int,
        country_codes: List[CountryCode] = None,
        networking: ContainerGroupNetworking = None,
        liveness_probe: ContainerGroupLivenessProbe = None,
        readiness_probe: ContainerGroupReadinessProbe = None,
        startup_probe: ContainerGroupStartupProbe = None,
        queue_connection: ContainerGroupQueueConnection = None,
    ):
        """Represents a container group

        :param id_: id_
        :type id_: str
        :param name: name
        :type name: str
        :param display_name: display_name
        :type display_name: str
        :param container: Represents a container
        :type container: Container
        :param autostart_policy: autostart_policy
        :type autostart_policy: bool
        :param restart_policy: restart_policy
        :type restart_policy: ContainerRestartPolicy
        :param replicas: replicas
        :type replicas: int
        :param current_state: Represents a container group state
        :type current_state: ContainerGroupState
        :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
        :type country_codes: List[CountryCode], optional
        :param networking: Represents container group networking parameters, defaults to None
        :type networking: ContainerGroupNetworking, optional
        :param liveness_probe: Represents the container group liveness probe, defaults to None
        :type liveness_probe: ContainerGroupLivenessProbe, optional
        :param readiness_probe: Represents the container group readiness probe, defaults to None
        :type readiness_probe: ContainerGroupReadinessProbe, optional
        :param startup_probe: Represents the container group startup probe, defaults to None
        :type startup_probe: ContainerGroupStartupProbe, optional
        :param queue_connection: Represents container group queue connection, defaults to None
        :type queue_connection: ContainerGroupQueueConnection, optional
        :param create_time: create_time
        :type create_time: str
        :param update_time: update_time
        :type update_time: str
        :param pending_change: pending_change
        :type pending_change: bool
        :param version: version
        :type version: int
        """
        self.id_ = id_
        self.name = self._define_str(
            "name",
            name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.display_name = self._define_str(
            "display_name",
            display_name,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.container = self._define_object(container, Container)
        self.autostart_policy = autostart_policy
        self.restart_policy = self._enum_matching(
            restart_policy, ContainerRestartPolicy.list(), "restart_policy"
        )
        self.replicas = self._define_number("replicas", replicas, ge=0, le=100)
        self.current_state = self._define_object(current_state, ContainerGroupState)
        self.country_codes = self._define_list(country_codes, CountryCode)
        self.networking = self._define_object(networking, ContainerGroupNetworking)
        self.liveness_probe = self._define_object(
            liveness_probe, ContainerGroupLivenessProbe
        )
        self.readiness_probe = self._define_object(
            readiness_probe, ContainerGroupReadinessProbe
        )
        self.startup_probe = self._define_object(
            startup_probe, ContainerGroupStartupProbe
        )
        self.queue_connection = self._define_object(
            queue_connection, ContainerGroupQueueConnection
        )
        self.create_time = create_time
        self.update_time = update_time
        self.pending_change = pending_change
        self.version = self._define_number("version", version, ge=1)
