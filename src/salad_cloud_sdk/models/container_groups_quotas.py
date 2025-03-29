from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class ContainerGroupsQuotas(BaseModel):
    """Represents the organization quotas for container groups

    :param container_replicas_quota: The maximum number of replicas that can be created for a container group
    :type container_replicas_quota: int
    :param container_replicas_used: The number of replicas that are currently in use
    :type container_replicas_used: int
    :param max_container_group_reallocations_per_minute: The maximum number of container group reallocations per minute, defaults to None
    :type max_container_group_reallocations_per_minute: int, optional
    :param max_container_group_recreates_per_minute: The maximum number of container group recreates per minute, defaults to None
    :type max_container_group_recreates_per_minute: int, optional
    :param max_container_group_restarts_per_minute: The maximum number of container group restarts per minute, defaults to None
    :type max_container_group_restarts_per_minute: int, optional
    """

    def __init__(
        self,
        container_replicas_quota: int,
        container_replicas_used: int,
        max_container_group_reallocations_per_minute: int = SENTINEL,
        max_container_group_recreates_per_minute: int = SENTINEL,
        max_container_group_restarts_per_minute: int = SENTINEL,
        **kwargs
    ):
        """Represents the organization quotas for container groups

        :param container_replicas_quota: The maximum number of replicas that can be created for a container group
        :type container_replicas_quota: int
        :param container_replicas_used: The number of replicas that are currently in use
        :type container_replicas_used: int
        :param max_container_group_reallocations_per_minute: The maximum number of container group reallocations per minute, defaults to None
        :type max_container_group_reallocations_per_minute: int, optional
        :param max_container_group_recreates_per_minute: The maximum number of container group recreates per minute, defaults to None
        :type max_container_group_recreates_per_minute: int, optional
        :param max_container_group_restarts_per_minute: The maximum number of container group restarts per minute, defaults to None
        :type max_container_group_restarts_per_minute: int, optional
        """
        self.container_replicas_quota = self._define_number(
            "container_replicas_quota", container_replicas_quota, ge=0, le=2147483647
        )
        self.container_replicas_used = self._define_number(
            "container_replicas_used", container_replicas_used, ge=0, le=2147483647
        )
        if max_container_group_reallocations_per_minute is not SENTINEL:
            self.max_container_group_reallocations_per_minute = self._define_number(
                "max_container_group_reallocations_per_minute",
                max_container_group_reallocations_per_minute,
                ge=0,
                le=2147483647,
            )
        if max_container_group_recreates_per_minute is not SENTINEL:
            self.max_container_group_recreates_per_minute = self._define_number(
                "max_container_group_recreates_per_minute",
                max_container_group_recreates_per_minute,
                ge=0,
                le=2147483647,
            )
        if max_container_group_restarts_per_minute is not SENTINEL:
            self.max_container_group_restarts_per_minute = self._define_number(
                "max_container_group_restarts_per_minute",
                max_container_group_restarts_per_minute,
                ge=0,
                le=2147483647,
            )
        self._kwargs = kwargs
