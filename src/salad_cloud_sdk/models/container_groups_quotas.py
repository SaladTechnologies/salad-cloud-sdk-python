from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class ContainerGroupsQuotas(BaseModel):
    """Represents the organization quotas for container groups

    :param max_created_container_groups: The maximum number of container groups that can be created, defaults to None
    :type max_created_container_groups: int, optional
    :param container_instance_quota: The maximum number of replicas that can be created for a container group, defaults to None
    :type container_instance_quota: int, optional
    :param container_replica_quota: The maximum number of replicas that can be created for a container group, defaults to None
    :type container_replica_quota: int, optional
    :param container_replicas_used: The number of replicas that are currently in use, defaults to None
    :type container_replicas_used: int, optional
    :param max_container_group_reallocations_per_minute: The maximum number of container group reallocations per minute, defaults to None
    :type max_container_group_reallocations_per_minute: int, optional
    :param max_container_group_recreates_per_minute: The maximum number of container group recreates per minute, defaults to None
    :type max_container_group_recreates_per_minute: int, optional
    :param max_container_group_restarts_per_minute: The maximum number of container group restarts per minute, defaults to None
    :type max_container_group_restarts_per_minute: int, optional
    """

    def __init__(
        self,
        max_created_container_groups: int = SENTINEL,
        container_instance_quota: int = SENTINEL,
        container_replica_quota: int = SENTINEL,
        container_replicas_used: int = SENTINEL,
        max_container_group_reallocations_per_minute: int = SENTINEL,
        max_container_group_recreates_per_minute: int = SENTINEL,
        max_container_group_restarts_per_minute: int = SENTINEL,
        **kwargs
    ):
        """Represents the organization quotas for container groups

        :param max_created_container_groups: The maximum number of container groups that can be created, defaults to None
        :type max_created_container_groups: int, optional
        :param container_instance_quota: The maximum number of replicas that can be created for a container group, defaults to None
        :type container_instance_quota: int, optional
        :param container_replica_quota: The maximum number of replicas that can be created for a container group, defaults to None
        :type container_replica_quota: int, optional
        :param container_replicas_used: The number of replicas that are currently in use, defaults to None
        :type container_replicas_used: int, optional
        :param max_container_group_reallocations_per_minute: The maximum number of container group reallocations per minute, defaults to None
        :type max_container_group_reallocations_per_minute: int, optional
        :param max_container_group_recreates_per_minute: The maximum number of container group recreates per minute, defaults to None
        :type max_container_group_recreates_per_minute: int, optional
        :param max_container_group_restarts_per_minute: The maximum number of container group restarts per minute, defaults to None
        :type max_container_group_restarts_per_minute: int, optional
        """
        if max_created_container_groups is not SENTINEL:
            self.max_created_container_groups = self._define_number(
                "max_created_container_groups",
                max_created_container_groups,
                ge=0,
                le=10000,
            )
        if container_instance_quota is not SENTINEL:
            self.container_instance_quota = self._define_number(
                "container_instance_quota", container_instance_quota, ge=0, le=500
            )
        if container_replica_quota is not SENTINEL:
            self.container_replica_quota = self._define_number(
                "container_replica_quota", container_replica_quota, ge=0, le=500
            )
        if container_replicas_used is not SENTINEL:
            self.container_replicas_used = self._define_number(
                "container_replicas_used", container_replicas_used, ge=0, le=500
            )
        if max_container_group_reallocations_per_minute is not SENTINEL:
            self.max_container_group_reallocations_per_minute = self._define_number(
                "max_container_group_reallocations_per_minute",
                max_container_group_reallocations_per_minute,
                ge=0,
                le=100,
            )
        if max_container_group_recreates_per_minute is not SENTINEL:
            self.max_container_group_recreates_per_minute = self._define_number(
                "max_container_group_recreates_per_minute",
                max_container_group_recreates_per_minute,
                ge=0,
                le=100,
            )
        if max_container_group_restarts_per_minute is not SENTINEL:
            self.max_container_group_restarts_per_minute = self._define_number(
                "max_container_group_restarts_per_minute",
                max_container_group_restarts_per_minute,
                ge=0,
                le=100,
            )
        self._kwargs = kwargs
