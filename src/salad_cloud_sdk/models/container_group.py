from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container import Container
from .country_code import CountryCode
from .container_group_state import ContainerGroupState
from .container_group_liveness_probe import ContainerGroupLivenessProbe
from .container_group_networking_configuration import (
    ContainerGroupNetworkingConfiguration,
)
from .container_group_priority import ContainerGroupPriority
from .queue_based_autoscaler_configuration import QueueBasedAutoscalerConfiguration
from .container_group_queue_connection import ContainerGroupQueueConnection
from .container_group_readiness_probe import ContainerGroupReadinessProbe
from .container_restart_policy import ContainerRestartPolicy
from .container_group_startup_probe import ContainerGroupStartupProbe


@JsonMap({"id_": "id"})
class ContainerGroup(BaseModel):
    """A container group definition that represents a scalable set of identical containers running as a distributed service

    :param autostart_policy: Defines whether containers in this group should automatically start when deployed (true) or require manual starting (false)
    :type autostart_policy: bool
    :param container: Represents a container with its configuration and resource requirements.
    :type container: Container
    :param country_codes: List of country codes where container instances are permitted to run. When not specified or empty, containers may run in any available region.
    :type country_codes: List[CountryCode]
    :param create_time: ISO 8601 timestamp when this container group was initially created
    :type create_time: str
    :param current_state: Represents the operational state of a container group during its lifecycle, including timing information, status, and instance distribution metrics. This state captures the current execution status, start and finish times, and provides visibility into the operational health across instances.
    :type current_state: ContainerGroupState
    :param display_name: The display-friendly name of the resource.
    :type display_name: str
    :param id_: The container group identifier.
    :type id_: str
    :param liveness_probe: Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy, defaults to None
    :type liveness_probe: ContainerGroupLivenessProbe, optional
    :param name: The container group name.
    :type name: str
    :param networking: Network configuration for container groups that defines connectivity, routing, and access control settings, defaults to None
    :type networking: ContainerGroupNetworkingConfiguration, optional
    :param organization_name: The organization name.
    :type organization_name: str
    :param pending_change: Indicates whether a configuration change has been requested but not yet applied to all containers in the group
    :type pending_change: bool
    :param priority: Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence.
    :type priority: ContainerGroupPriority
    :param project_name: The project name.
    :type project_name: str
    :param queue_autoscaler: Defines configuration for automatically scaling container instances based on queue length. The autoscaler monitors a queue and adjusts the number of running replicas to maintain the desired queue length., defaults to None
    :type queue_autoscaler: QueueBasedAutoscalerConfiguration, optional
    :param queue_connection: Configuration for connecting a container group to a message queue system, enabling asynchronous communication between services., defaults to None
    :type queue_connection: ContainerGroupQueueConnection, optional
    :param readiness_probe: Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it., defaults to None
    :type readiness_probe: ContainerGroupReadinessProbe, optional
    :param readme: readme, defaults to None
    :type readme: str, optional
    :param replicas: The container group replicas.
    :type replicas: int
    :param restart_policy: Specifies the policy for restarting containers when they exit or fail.
    :type restart_policy: ContainerRestartPolicy
    :param startup_probe: Defines a probe that checks if a container application has started successfully. Startup probes help prevent applications from being prematurely marked as unhealthy during initialization. The probe can use HTTP requests, TCP connections, gRPC calls, or shell commands to determine startup status., defaults to None
    :type startup_probe: ContainerGroupStartupProbe, optional
    :param update_time: ISO 8601 timestamp when this container group was last updated
    :type update_time: str
    :param version: Incremental version number that increases with each configuration change to the container group
    :type version: int
    """

    def __init__(
        self,
        autostart_policy: bool,
        container: Container,
        country_codes: List[CountryCode],
        create_time: str,
        current_state: ContainerGroupState,
        display_name: str,
        id_: str,
        name: str,
        organization_name: str,
        pending_change: bool,
        priority: Union[ContainerGroupPriority, None],
        project_name: str,
        replicas: int,
        restart_policy: ContainerRestartPolicy,
        update_time: str,
        version: int,
        liveness_probe: Union[ContainerGroupLivenessProbe, None] = SENTINEL,
        networking: ContainerGroupNetworkingConfiguration = SENTINEL,
        queue_autoscaler: QueueBasedAutoscalerConfiguration = SENTINEL,
        queue_connection: ContainerGroupQueueConnection = SENTINEL,
        readiness_probe: Union[ContainerGroupReadinessProbe, None] = SENTINEL,
        readme: str = SENTINEL,
        startup_probe: Union[ContainerGroupStartupProbe, None] = SENTINEL,
        **kwargs,
    ):
        """A container group definition that represents a scalable set of identical containers running as a distributed service

        :param autostart_policy: Defines whether containers in this group should automatically start when deployed (true) or require manual starting (false)
        :type autostart_policy: bool
        :param container: Represents a container with its configuration and resource requirements.
        :type container: Container
        :param country_codes: List of country codes where container instances are permitted to run. When not specified or empty, containers may run in any available region.
        :type country_codes: List[CountryCode]
        :param create_time: ISO 8601 timestamp when this container group was initially created
        :type create_time: str
        :param current_state: Represents the operational state of a container group during its lifecycle, including timing information, status, and instance distribution metrics. This state captures the current execution status, start and finish times, and provides visibility into the operational health across instances.
        :type current_state: ContainerGroupState
        :param display_name: The display-friendly name of the resource.
        :type display_name: str
        :param id_: The container group identifier.
        :type id_: str
        :param liveness_probe: Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy, defaults to None
        :type liveness_probe: ContainerGroupLivenessProbe, optional
        :param name: The container group name.
        :type name: str
        :param networking: Network configuration for container groups that defines connectivity, routing, and access control settings, defaults to None
        :type networking: ContainerGroupNetworkingConfiguration, optional
        :param organization_name: The organization name.
        :type organization_name: str
        :param pending_change: Indicates whether a configuration change has been requested but not yet applied to all containers in the group
        :type pending_change: bool
        :param priority: Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence.
        :type priority: ContainerGroupPriority
        :param project_name: The project name.
        :type project_name: str
        :param queue_autoscaler: Defines configuration for automatically scaling container instances based on queue length. The autoscaler monitors a queue and adjusts the number of running replicas to maintain the desired queue length., defaults to None
        :type queue_autoscaler: QueueBasedAutoscalerConfiguration, optional
        :param queue_connection: Configuration for connecting a container group to a message queue system, enabling asynchronous communication between services., defaults to None
        :type queue_connection: ContainerGroupQueueConnection, optional
        :param readiness_probe: Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it., defaults to None
        :type readiness_probe: ContainerGroupReadinessProbe, optional
        :param readme: readme, defaults to None
        :type readme: str, optional
        :param replicas: The container group replicas.
        :type replicas: int
        :param restart_policy: Specifies the policy for restarting containers when they exit or fail.
        :type restart_policy: ContainerRestartPolicy
        :param startup_probe: Defines a probe that checks if a container application has started successfully. Startup probes help prevent applications from being prematurely marked as unhealthy during initialization. The probe can use HTTP requests, TCP connections, gRPC calls, or shell commands to determine startup status., defaults to None
        :type startup_probe: ContainerGroupStartupProbe, optional
        :param update_time: ISO 8601 timestamp when this container group was last updated
        :type update_time: str
        :param version: Incremental version number that increases with each configuration change to the container group
        :type version: int
        """
        self.autostart_policy = autostart_policy
        self.container = self._define_object(container, Container)
        self.country_codes = self._define_list(country_codes, CountryCode)
        self.create_time = create_time
        self.current_state = self._define_object(current_state, ContainerGroupState)
        self.display_name = self._define_str(
            "display_name",
            display_name,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.id_ = id_
        if liveness_probe is not SENTINEL:
            self.liveness_probe = self._define_object(
                liveness_probe, ContainerGroupLivenessProbe
            )
        self.name = self._define_str(
            "name",
            name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        if networking is not SENTINEL:
            self.networking = self._define_object(
                networking, ContainerGroupNetworkingConfiguration
            )
        self.organization_name = self._define_str(
            "organization_name",
            organization_name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.pending_change = pending_change
        self.priority = self._enum_matching(
            priority, ContainerGroupPriority.list(), "priority"
        )
        self.project_name = self._define_str(
            "project_name",
            project_name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        if queue_autoscaler is not SENTINEL:
            self.queue_autoscaler = self._define_object(
                queue_autoscaler, QueueBasedAutoscalerConfiguration
            )
        if queue_connection is not SENTINEL:
            self.queue_connection = self._define_object(
                queue_connection, ContainerGroupQueueConnection
            )
        if readiness_probe is not SENTINEL:
            self.readiness_probe = self._define_object(
                readiness_probe, ContainerGroupReadinessProbe
            )
        if readme is not SENTINEL:
            self.readme = self._define_str(
                "readme", readme, min_length=2, max_length=65000
            )
        self.replicas = self._define_number("replicas", replicas, ge=0, le=500)
        self.restart_policy = self._enum_matching(
            restart_policy, ContainerRestartPolicy.list(), "restart_policy"
        )
        if startup_probe is not SENTINEL:
            self.startup_probe = self._define_object(
                startup_probe, ContainerGroupStartupProbe
            )
        self.update_time = update_time
        self.version = self._define_number("version", version, ge=1, le=2147483647)
        self._kwargs = kwargs
