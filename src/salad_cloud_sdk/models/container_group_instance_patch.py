from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class ContainerGroupInstancePatch(BaseModel):
    """Represents a request to update a container group instance

    :param deletion_cost: The cost of deleting the container group instance, defaults to None
    :type deletion_cost: int, optional
    """

    def __init__(self, deletion_cost: Union[int, None] = SENTINEL, **kwargs):
        """Represents a request to update a container group instance

        :param deletion_cost: The cost of deleting the container group instance, defaults to None
        :type deletion_cost: int, optional
        """
        if deletion_cost is not SENTINEL:
            self.deletion_cost = self._define_number(
                "deletion_cost", deletion_cost, nullable=True, ge=0, le=100000
            )
        self._kwargs = kwargs
