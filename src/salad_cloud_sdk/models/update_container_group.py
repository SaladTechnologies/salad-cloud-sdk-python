from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .update_container import UpdateContainer
from .country_code import CountryCode
from .update_container_group_networking import UpdateContainerGroupNetworking
from .container_group_liveness_probe import ContainerGroupLivenessProbe
from .container_group_readiness_probe import ContainerGroupReadinessProbe
from .container_group_startup_probe import ContainerGroupStartupProbe
from .queue_autoscaler import QueueAutoscaler


@JsonMap({})
class UpdateContainerGroup(BaseModel):
    """Represents a request to update a container group

    :param display_name: display_name, defaults to None
    :type display_name: str, optional
    :param container: Represents an update container object, defaults to None
    :type container: UpdateContainer, optional
    :param replicas: replicas, defaults to None
    :type replicas: int, optional
    :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
    :type country_codes: List[CountryCode], optional
    :param networking: Represents update container group networking parameters, defaults to None
    :type networking: UpdateContainerGroupNetworking, optional
    :param liveness_probe: Represents the container group liveness probe, defaults to None
    :type liveness_probe: ContainerGroupLivenessProbe, optional
    :param readiness_probe: Represents the container group readiness probe, defaults to None
    :type readiness_probe: ContainerGroupReadinessProbe, optional
    :param startup_probe: Represents the container group startup probe, defaults to None
    :type startup_probe: ContainerGroupStartupProbe, optional
    :param queue_autoscaler: Represents the autoscaling rules for a queue, defaults to None
    :type queue_autoscaler: QueueAutoscaler, optional
    """

    def __init__(
        self,
        display_name: Union[str, None] = SENTINEL,
        container: Union[UpdateContainer, None] = SENTINEL,
        replicas: Union[int, None] = SENTINEL,
        country_codes: Union[List[CountryCode], None] = SENTINEL,
        networking: UpdateContainerGroupNetworking = SENTINEL,
        liveness_probe: Union[ContainerGroupLivenessProbe, None] = SENTINEL,
        readiness_probe: Union[ContainerGroupReadinessProbe, None] = SENTINEL,
        startup_probe: Union[ContainerGroupStartupProbe, None] = SENTINEL,
        queue_autoscaler: Union[QueueAutoscaler, None] = SENTINEL,
        **kwargs,
    ):
        """Represents a request to update a container group

        :param display_name: display_name, defaults to None
        :type display_name: str, optional
        :param container: Represents an update container object, defaults to None
        :type container: UpdateContainer, optional
        :param replicas: replicas, defaults to None
        :type replicas: int, optional
        :param country_codes: List of countries nodes must be located in. Remove this field to permit nodes from any country., defaults to None
        :type country_codes: List[CountryCode], optional
        :param networking: Represents update container group networking parameters, defaults to None
        :type networking: UpdateContainerGroupNetworking, optional
        :param liveness_probe: Represents the container group liveness probe, defaults to None
        :type liveness_probe: ContainerGroupLivenessProbe, optional
        :param readiness_probe: Represents the container group readiness probe, defaults to None
        :type readiness_probe: ContainerGroupReadinessProbe, optional
        :param startup_probe: Represents the container group startup probe, defaults to None
        :type startup_probe: ContainerGroupStartupProbe, optional
        :param queue_autoscaler: Represents the autoscaling rules for a queue, defaults to None
        :type queue_autoscaler: QueueAutoscaler, optional
        """
        if display_name is not SENTINEL:
            self.display_name = self._define_str(
                "display_name",
                display_name,
                nullable=True,
                pattern="^[ ,-.0-9A-Za-z]+$",
                min_length=2,
                max_length=63,
            )
        if container is not SENTINEL:
            self.container = self._define_object(container, UpdateContainer)
        if replicas is not SENTINEL:
            self.replicas = self._define_number(
                "replicas", replicas, nullable=True, ge=0, le=500
            )
        if country_codes is not SENTINEL:
            self.country_codes = self._define_list(country_codes, CountryCode)
        if networking is not SENTINEL:
            self.networking = self._define_object(
                networking, UpdateContainerGroupNetworking
            )
        if liveness_probe is not SENTINEL:
            self.liveness_probe = self._define_object(
                liveness_probe, ContainerGroupLivenessProbe
            )
        if readiness_probe is not SENTINEL:
            self.readiness_probe = self._define_object(
                readiness_probe, ContainerGroupReadinessProbe
            )
        if startup_probe is not SENTINEL:
            self.startup_probe = self._define_object(
                startup_probe, ContainerGroupStartupProbe
            )
        if queue_autoscaler is not SENTINEL:
            self.queue_autoscaler = self._define_object(
                queue_autoscaler, QueueAutoscaler
            )
        self._kwargs = kwargs
