from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupsQuotas(BaseModel):
    """ContainerGroupsQuotas

    :param max_created_container_groups: max_created_container_groups
    :type max_created_container_groups: int
    :param container_instance_quota: container_instance_quota
    :type container_instance_quota: int
    :param max_container_group_reallocations_per_minute: max_container_group_reallocations_per_minute, defaults to None
    :type max_container_group_reallocations_per_minute: int, optional
    :param max_container_group_recreates_per_minute: max_container_group_recreates_per_minute, defaults to None
    :type max_container_group_recreates_per_minute: int, optional
    :param max_container_group_restarts_per_minute: max_container_group_restarts_per_minute, defaults to None
    :type max_container_group_restarts_per_minute: int, optional
    """

    def __init__(
        self,
        max_created_container_groups: int,
        container_instance_quota: int,
        max_container_group_reallocations_per_minute: int = None,
        max_container_group_recreates_per_minute: int = None,
        max_container_group_restarts_per_minute: int = None,
    ):
        """ContainerGroupsQuotas

        :param max_created_container_groups: max_created_container_groups
        :type max_created_container_groups: int
        :param container_instance_quota: container_instance_quota
        :type container_instance_quota: int
        :param max_container_group_reallocations_per_minute: max_container_group_reallocations_per_minute, defaults to None
        :type max_container_group_reallocations_per_minute: int, optional
        :param max_container_group_recreates_per_minute: max_container_group_recreates_per_minute, defaults to None
        :type max_container_group_recreates_per_minute: int, optional
        :param max_container_group_restarts_per_minute: max_container_group_restarts_per_minute, defaults to None
        :type max_container_group_restarts_per_minute: int, optional
        """
        self.max_created_container_groups = max_created_container_groups
        self.container_instance_quota = container_instance_quota
        self.max_container_group_reallocations_per_minute = self._define_number(
            "max_container_group_reallocations_per_minute",
            max_container_group_reallocations_per_minute,
            nullable=True,
            ge=0,
        )
        self.max_container_group_recreates_per_minute = self._define_number(
            "max_container_group_recreates_per_minute",
            max_container_group_recreates_per_minute,
            nullable=True,
            ge=0,
        )
        self.max_container_group_restarts_per_minute = self._define_number(
            "max_container_group_restarts_per_minute",
            max_container_group_restarts_per_minute,
            nullable=True,
            ge=0,
        )
