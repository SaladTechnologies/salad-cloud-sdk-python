from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .create_container import CreateContainer
from .container_restart_policy import ContainerRestartPolicy
from .country_code import CountryCode
from .create_container_group_networking import CreateContainerGroupNetworking
from .container_group_liveness_probe import ContainerGroupLivenessProbe
from .container_group_readiness_probe import ContainerGroupReadinessProbe
from .container_group_startup_probe import ContainerGroupStartupProbe
from .container_group_queue_connection import ContainerGroupQueueConnection


@JsonMap({})
class CreateContainerGroup(BaseModel):
    """Represents a request to create a container group

    :param name: name
    :type name: str
    :param display_name: display_name, defaults to None
    :type display_name: str, optional
    :param container: Represents a container
    :type container: CreateContainer
    :param autostart_policy: autostart_policy
    :type autostart_policy: bool
    :param restart_policy: restart_policy
    :type restart_policy: ContainerRestartPolicy
    :param replicas: replicas
    :type replicas: int
    :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
    :type country_codes: List[CountryCode], optional
    :param networking: Represents container group networking parameters, defaults to None
    :type networking: CreateContainerGroupNetworking, optional
    :param liveness_probe: Represents the container group liveness probe, defaults to None
    :type liveness_probe: ContainerGroupLivenessProbe, optional
    :param readiness_probe: Represents the container group readiness probe, defaults to None
    :type readiness_probe: ContainerGroupReadinessProbe, optional
    :param startup_probe: Represents the container group startup probe, defaults to None
    :type startup_probe: ContainerGroupStartupProbe, optional
    :param queue_connection: Represents container group queue connection, defaults to None
    :type queue_connection: ContainerGroupQueueConnection, optional
    """

    def __init__(
        self,
        name: str,
        container: CreateContainer,
        autostart_policy: bool,
        restart_policy: ContainerRestartPolicy,
        replicas: int,
        display_name: str = None,
        country_codes: List[CountryCode] = None,
        networking: CreateContainerGroupNetworking = None,
        liveness_probe: ContainerGroupLivenessProbe = None,
        readiness_probe: ContainerGroupReadinessProbe = None,
        startup_probe: ContainerGroupStartupProbe = None,
        queue_connection: ContainerGroupQueueConnection = None,
    ):
        """Represents a request to create a container group

        :param name: name
        :type name: str
        :param display_name: display_name, defaults to None
        :type display_name: str, optional
        :param container: Represents a container
        :type container: CreateContainer
        :param autostart_policy: autostart_policy
        :type autostart_policy: bool
        :param restart_policy: restart_policy
        :type restart_policy: ContainerRestartPolicy
        :param replicas: replicas
        :type replicas: int
        :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
        :type country_codes: List[CountryCode], optional
        :param networking: Represents container group networking parameters, defaults to None
        :type networking: CreateContainerGroupNetworking, optional
        :param liveness_probe: Represents the container group liveness probe, defaults to None
        :type liveness_probe: ContainerGroupLivenessProbe, optional
        :param readiness_probe: Represents the container group readiness probe, defaults to None
        :type readiness_probe: ContainerGroupReadinessProbe, optional
        :param startup_probe: Represents the container group startup probe, defaults to None
        :type startup_probe: ContainerGroupStartupProbe, optional
        :param queue_connection: Represents container group queue connection, defaults to None
        :type queue_connection: ContainerGroupQueueConnection, optional
        """
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
            nullable=True,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.container = self._define_object(container, CreateContainer)
        self.autostart_policy = autostart_policy
        self.restart_policy = self._enum_matching(
            restart_policy, ContainerRestartPolicy.list(), "restart_policy"
        )
        self.replicas = self._define_number("replicas", replicas, ge=0, le=250)
        self.country_codes = self._define_list(country_codes, CountryCode)
        self.networking = self._define_object(
            networking, CreateContainerGroupNetworking
        )
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
