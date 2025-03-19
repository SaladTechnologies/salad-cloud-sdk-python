from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_configuration import ContainerConfiguration
from .country_code import CountryCode
from .container_group_liveness_probe import ContainerGroupLivenessProbe
from .create_container_group_networking import CreateContainerGroupNetworking
from .queue_based_autoscaler_configuration import QueueBasedAutoscalerConfiguration
from .container_group_queue_connection import ContainerGroupQueueConnection
from .container_group_readiness_probe import ContainerGroupReadinessProbe
from .container_restart_policy import ContainerRestartPolicy
from .container_group_startup_probe import ContainerGroupStartupProbe


@JsonMap({})
class ContainerGroupCreationRequest(BaseModel):
    """Represents a request to create a container group, which manages a collection of container instances with shared configuration and scaling policies

    :param autostart_policy: Determines whether the container group should start automatically when created (true) or remain stopped until manually started (false)
    :type autostart_policy: bool
    :param container: Configuration for creating a container within a container group. Defines the container image, resource requirements, environment variables, and other settings needed to deploy and run the container.
    :type container: ContainerConfiguration
    :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
    :type country_codes: List[CountryCode], optional
    :param display_name: Human-readable name for the container group that can include spaces and special characters, used for display purposes, defaults to None
    :type display_name: str, optional
    :param liveness_probe: Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy, defaults to None
    :type liveness_probe: ContainerGroupLivenessProbe, optional
    :param name: Unique identifier for the container group that must follow DNS naming conventions (lowercase alphanumeric with hyphens)
    :type name: str
    :param networking: Network configuration for container groups specifying connectivity parameters, including authentication, protocol, and timeout settings, defaults to None
    :type networking: CreateContainerGroupNetworking, optional
    :param queue_autoscaler: Defines configuration for automatically scaling container instances based on queue length. The autoscaler monitors a queue and adjusts the number of running replicas to maintain the desired queue length., defaults to None
    :type queue_autoscaler: QueueBasedAutoscalerConfiguration, optional
    :param queue_connection: Configuration for connecting a container group to a message queue system, enabling asynchronous communication between services., defaults to None
    :type queue_connection: ContainerGroupQueueConnection, optional
    :param readiness_probe: Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it., defaults to None
    :type readiness_probe: ContainerGroupReadinessProbe, optional
    :param replicas: Number of container instances to deploy and maintain for this container group
    :type replicas: int
    :param restart_policy: Specifies the policy for restarting containers when they exit or fail.
    :type restart_policy: ContainerRestartPolicy
    :param startup_probe: Defines a probe that checks if a container application has started successfully. Startup probes help prevent applications from being prematurely marked as unhealthy during initialization. The probe can use HTTP requests, TCP connections, gRPC calls, or shell commands to determine startup status., defaults to None
    :type startup_probe: ContainerGroupStartupProbe, optional
    """

    def __init__(
        self,
        autostart_policy: bool,
        container: ContainerConfiguration,
        name: str,
        replicas: int,
        restart_policy: ContainerRestartPolicy,
        country_codes: List[CountryCode] = SENTINEL,
        display_name: str = SENTINEL,
        liveness_probe: Union[ContainerGroupLivenessProbe, None] = SENTINEL,
        networking: CreateContainerGroupNetworking = SENTINEL,
        queue_autoscaler: QueueBasedAutoscalerConfiguration = SENTINEL,
        queue_connection: ContainerGroupQueueConnection = SENTINEL,
        readiness_probe: Union[ContainerGroupReadinessProbe, None] = SENTINEL,
        startup_probe: Union[ContainerGroupStartupProbe, None] = SENTINEL,
        **kwargs,
    ):
        """Represents a request to create a container group, which manages a collection of container instances with shared configuration and scaling policies

        :param autostart_policy: Determines whether the container group should start automatically when created (true) or remain stopped until manually started (false)
        :type autostart_policy: bool
        :param container: Configuration for creating a container within a container group. Defines the container image, resource requirements, environment variables, and other settings needed to deploy and run the container.
        :type container: ContainerConfiguration
        :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
        :type country_codes: List[CountryCode], optional
        :param display_name: Human-readable name for the container group that can include spaces and special characters, used for display purposes, defaults to None
        :type display_name: str, optional
        :param liveness_probe: Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy, defaults to None
        :type liveness_probe: ContainerGroupLivenessProbe, optional
        :param name: Unique identifier for the container group that must follow DNS naming conventions (lowercase alphanumeric with hyphens)
        :type name: str
        :param networking: Network configuration for container groups specifying connectivity parameters, including authentication, protocol, and timeout settings, defaults to None
        :type networking: CreateContainerGroupNetworking, optional
        :param queue_autoscaler: Defines configuration for automatically scaling container instances based on queue length. The autoscaler monitors a queue and adjusts the number of running replicas to maintain the desired queue length., defaults to None
        :type queue_autoscaler: QueueBasedAutoscalerConfiguration, optional
        :param queue_connection: Configuration for connecting a container group to a message queue system, enabling asynchronous communication between services., defaults to None
        :type queue_connection: ContainerGroupQueueConnection, optional
        :param readiness_probe: Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it., defaults to None
        :type readiness_probe: ContainerGroupReadinessProbe, optional
        :param replicas: Number of container instances to deploy and maintain for this container group
        :type replicas: int
        :param restart_policy: Specifies the policy for restarting containers when they exit or fail.
        :type restart_policy: ContainerRestartPolicy
        :param startup_probe: Defines a probe that checks if a container application has started successfully. Startup probes help prevent applications from being prematurely marked as unhealthy during initialization. The probe can use HTTP requests, TCP connections, gRPC calls, or shell commands to determine startup status., defaults to None
        :type startup_probe: ContainerGroupStartupProbe, optional
        """
        self.autostart_policy = autostart_policy
        self.container = self._define_object(container, ContainerConfiguration)
        if country_codes is not SENTINEL:
            self.country_codes = self._define_list(country_codes, CountryCode)
        if display_name is not SENTINEL:
            self.display_name = self._define_str(
                "display_name",
                display_name,
                pattern="^[ ,-.0-9A-Za-z]+$",
                min_length=2,
                max_length=63,
            )
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
                networking, CreateContainerGroupNetworking
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
        self.replicas = self._define_number("replicas", replicas, ge=0, le=500)
        self.restart_policy = self._enum_matching(
            restart_policy, ContainerRestartPolicy.list(), "restart_policy"
        )
        if startup_probe is not SENTINEL:
            self.startup_probe = self._define_object(
                startup_probe, ContainerGroupStartupProbe
            )
        self._kwargs = kwargs
