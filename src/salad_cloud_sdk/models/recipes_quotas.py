from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class RecipesQuotas(BaseModel):
    """RecipesQuotas

    :param max_created_recipe_deployments: max_created_recipe_deployments
    :type max_created_recipe_deployments: int
    :param recipe_instance_quota: recipe_instance_quota
    :type recipe_instance_quota: int
    """

    def __init__(self, max_created_recipe_deployments: int, recipe_instance_quota: int):
        """RecipesQuotas

        :param max_created_recipe_deployments: max_created_recipe_deployments
        :type max_created_recipe_deployments: int
        :param recipe_instance_quota: recipe_instance_quota
        :type recipe_instance_quota: int
        """
        self.max_created_recipe_deployments = max_created_recipe_deployments
        self.recipe_instance_quota = recipe_instance_quota
