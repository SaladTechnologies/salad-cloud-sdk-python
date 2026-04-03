from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .update_container import UpdateContainer
from .country_code import CountryCode
from .container_group_liveness_probe import ContainerGroupLivenessProbe
from .update_container_group_networking import UpdateContainerGroupNetworking
from .queue_based_autoscaler_configuration import QueueBasedAutoscalerConfiguration
from .container_group_readiness_probe import ContainerGroupReadinessProbe
from .container_group_scaling_action import ContainerGroupScalingAction
from .container_group_startup_probe import ContainerGroupStartupProbe


@JsonMap(
    {
        "scaling_actions": "scaling-actions",
        "scheduled_scaling_enabled": "scheduled-scaling-enabled",
    }
)
class ContainerGroupPatch(BaseModel):
    """Represents a request to update a container group

    :param container: Represents an update container object, defaults to None
    :type container: UpdateContainer, optional
    :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
    :type country_codes: List[CountryCode], optional
    :param display_name: The display name for the container group. If null is provided, the display name will be set to the container group name., defaults to None
    :type display_name: str, optional
    :param liveness_probe: Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy, defaults to None
    :type liveness_probe: ContainerGroupLivenessProbe, optional
    :param networking: Represents update container group networking parameters, defaults to None
    :type networking: UpdateContainerGroupNetworking, optional
    :param queue_autoscaler: Defines configuration for automatically scaling container instances based on queue length. The autoscaler monitors a queue and adjusts the number of running replicas to maintain the desired queue length., defaults to None
    :type queue_autoscaler: QueueBasedAutoscalerConfiguration, optional
    :param readiness_probe: Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it., defaults to None
    :type readiness_probe: ContainerGroupReadinessProbe, optional
    :param replicas: The desired number of instances for your container group deployment., defaults to None
    :type replicas: int, optional
    :param scaling_actions: List of scaling actions configurations, defaults to None
    :type scaling_actions: List[ContainerGroupScalingAction], optional
    :param scheduled_scaling_enabled: Indicates if scheduled scaling is enabled, defaults to None
    :type scheduled_scaling_enabled: bool, optional
    :param startup_probe: Defines a probe that checks if a container application has started successfully. Startup probes help prevent applications from being prematurely marked as unhealthy during initialization. The probe can use HTTP requests, TCP connections, gRPC calls, or shell commands to determine startup status., defaults to None
    :type startup_probe: ContainerGroupStartupProbe, optional
    """

    def __init__(
        self,
        container: Union[UpdateContainer, None] = SENTINEL,
        country_codes: Union[List[CountryCode], None] = SENTINEL,
        display_name: Union[str, None] = SENTINEL,
        liveness_probe: Union[ContainerGroupLivenessProbe, None] = SENTINEL,
        networking: UpdateContainerGroupNetworking = SENTINEL,
        queue_autoscaler: QueueBasedAutoscalerConfiguration = SENTINEL,
        readiness_probe: Union[ContainerGroupReadinessProbe, None] = SENTINEL,
        replicas: Union[int, None] = SENTINEL,
        scaling_actions: List[ContainerGroupScalingAction] = SENTINEL,
        scheduled_scaling_enabled: bool = SENTINEL,
        startup_probe: Union[ContainerGroupStartupProbe, None] = SENTINEL,
        **kwargs,
    ):
        """Represents a request to update a container group

        :param container: Represents an update container object, defaults to None
        :type container: UpdateContainer, optional
        :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
        :type country_codes: List[CountryCode], optional
        :param display_name: The display name for the container group. If null is provided, the display name will be set to the container group name., defaults to None
        :type display_name: str, optional
        :param liveness_probe: Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy, defaults to None
        :type liveness_probe: ContainerGroupLivenessProbe, optional
        :param networking: Represents update container group networking parameters, defaults to None
        :type networking: UpdateContainerGroupNetworking, optional
        :param queue_autoscaler: Defines configuration for automatically scaling container instances based on queue length. The autoscaler monitors a queue and adjusts the number of running replicas to maintain the desired queue length., defaults to None
        :type queue_autoscaler: QueueBasedAutoscalerConfiguration, optional
        :param readiness_probe: Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it., defaults to None
        :type readiness_probe: ContainerGroupReadinessProbe, optional
        :param replicas: The desired number of instances for your container group deployment., defaults to None
        :type replicas: int, optional
        :param scaling_actions: List of scaling actions configurations, defaults to None
        :type scaling_actions: List[ContainerGroupScalingAction], optional
        :param scheduled_scaling_enabled: Indicates if scheduled scaling is enabled, defaults to None
        :type scheduled_scaling_enabled: bool, optional
        :param startup_probe: Defines a probe that checks if a container application has started successfully. Startup probes help prevent applications from being prematurely marked as unhealthy during initialization. The probe can use HTTP requests, TCP connections, gRPC calls, or shell commands to determine startup status., defaults to None
        :type startup_probe: ContainerGroupStartupProbe, optional
        """
        if container is not SENTINEL:
            self.container = self._define_object(
                container, UpdateContainer, nullable=True
            )
        if country_codes is not SENTINEL:
            self.country_codes = self._define_list(
                country_codes, CountryCode, nullable=True
            )
        if display_name is not SENTINEL:
            self.display_name = self._define_str(
                "display_name",
                display_name,
                nullable=True,
                pattern="^[ ,-.0-9A-Za-z]+$",
                min_length=2,
                max_length=63,
            )
        if liveness_probe is not SENTINEL:
            self.liveness_probe = self._define_object(
                liveness_probe, ContainerGroupLivenessProbe, nullable=True
            )
        if networking is not SENTINEL:
            self.networking = self._define_object(
                networking, UpdateContainerGroupNetworking
            )
        if queue_autoscaler is not SENTINEL:
            self.queue_autoscaler = self._define_object(
                queue_autoscaler, QueueBasedAutoscalerConfiguration
            )
        if readiness_probe is not SENTINEL:
            self.readiness_probe = self._define_object(
                readiness_probe, ContainerGroupReadinessProbe, nullable=True
            )
        if replicas is not SENTINEL:
            self.replicas = self._define_number(
                "replicas", replicas, nullable=True, ge=0, le=500
            )
        if scaling_actions is not SENTINEL:
            self.scaling_actions = self._define_list(
                scaling_actions, ContainerGroupScalingAction
            )
        if scheduled_scaling_enabled is not SENTINEL:
            self.scheduled_scaling_enabled = scheduled_scaling_enabled
        if startup_probe is not SENTINEL:
            self.startup_probe = self._define_object(
                startup_probe, ContainerGroupStartupProbe, nullable=True
            )
        self._kwargs = kwargs
