from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_groups_quotas import ContainerGroupsQuotas
from .recipes_quotas import RecipesQuotas


@JsonMap({})
class Quotas(BaseModel):
    """Represents the organization quotas

    :param container_groups_quotas: container_groups_quotas
    :type container_groups_quotas: ContainerGroupsQuotas
    :param create_time: The time the resource was created, defaults to None
    :type create_time: str, optional
    :param recipes_quotas: recipes_quotas
    :type recipes_quotas: RecipesQuotas
    :param update_time: The time the resource was last updated, defaults to None
    :type update_time: str, optional
    """

    def __init__(
        self,
        container_groups_quotas: ContainerGroupsQuotas,
        recipes_quotas: RecipesQuotas,
        create_time: str = None,
        update_time: str = None,
    ):
        """Represents the organization quotas

        :param container_groups_quotas: container_groups_quotas
        :type container_groups_quotas: ContainerGroupsQuotas
        :param create_time: The time the resource was created, defaults to None
        :type create_time: str, optional
        :param recipes_quotas: recipes_quotas
        :type recipes_quotas: RecipesQuotas
        :param update_time: The time the resource was last updated, defaults to None
        :type update_time: str, optional
        """
        self.container_groups_quotas = self._define_object(
            container_groups_quotas, ContainerGroupsQuotas
        )
        if create_time is not None:
            self.create_time = create_time
        self.recipes_quotas = self._define_object(recipes_quotas, RecipesQuotas)
        if update_time is not None:
            self.update_time = update_time
