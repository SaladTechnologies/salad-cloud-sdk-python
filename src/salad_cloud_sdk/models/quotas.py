from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_groups_quotas import ContainerGroupsQuotas


@JsonMap({})
class Quotas(BaseModel):
    """Represents the organization quotas

    :param container_groups_quotas: Represents the organization quotas for container groups
    :type container_groups_quotas: ContainerGroupsQuotas
    :param create_time: The time the resource was created, defaults to None
    :type create_time: str, optional
    :param update_time: The time the resource was last updated, defaults to None
    :type update_time: str, optional
    """

    def __init__(
        self,
        container_groups_quotas: ContainerGroupsQuotas,
        create_time: str = SENTINEL,
        update_time: str = SENTINEL,
        **kwargs,
    ):
        """Represents the organization quotas

        :param container_groups_quotas: Represents the organization quotas for container groups
        :type container_groups_quotas: ContainerGroupsQuotas
        :param create_time: The time the resource was created, defaults to None
        :type create_time: str, optional
        :param update_time: The time the resource was last updated, defaults to None
        :type update_time: str, optional
        """
        self.container_groups_quotas = self._define_object(
            container_groups_quotas, ContainerGroupsQuotas
        )
        if create_time is not SENTINEL:
            self.create_time = create_time
        if update_time is not SENTINEL:
            self.update_time = update_time
        self._kwargs = kwargs
