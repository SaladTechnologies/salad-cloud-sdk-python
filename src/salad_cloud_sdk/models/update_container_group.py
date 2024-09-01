from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .update_container import UpdateContainer
from .country_code import CountryCode
from .update_container_group_networking import UpdateContainerGroupNetworking
from .container_group_liveness_probe import ContainerGroupLivenessProbe
from .container_group_readiness_probe import ContainerGroupReadinessProbe
from .container_group_startup_probe import ContainerGroupStartupProbe


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
    """

    def __init__(
        self,
        display_name: str = None,
        container: UpdateContainer = None,
        replicas: int = None,
        country_codes: List[CountryCode] = None,
        networking: UpdateContainerGroupNetworking = None,
        liveness_probe: ContainerGroupLivenessProbe = None,
        readiness_probe: ContainerGroupReadinessProbe = None,
        startup_probe: ContainerGroupStartupProbe = None,
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
        """
        self.display_name = self._define_str(
            "display_name",
            display_name,
            nullable=True,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.container = self._define_object(container, UpdateContainer)
        self.replicas = self._define_number(
            "replicas", replicas, nullable=True, ge=0, le=250
        )
        self.country_codes = self._define_list(country_codes, CountryCode)
        self.networking = self._define_object(
            networking, UpdateContainerGroupNetworking
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
