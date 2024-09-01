from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupInstanceStatusCount(BaseModel):
    """Represents a container group instance status count

    :param allocating_count: allocating_count
    :type allocating_count: int
    :param creating_count: creating_count
    :type creating_count: int
    :param running_count: running_count
    :type running_count: int
    :param stopping_count: stopping_count
    :type stopping_count: int
    """

    def __init__(
        self,
        allocating_count: int,
        creating_count: int,
        running_count: int,
        stopping_count: int,
    ):
        """Represents a container group instance status count

        :param allocating_count: allocating_count
        :type allocating_count: int
        :param creating_count: creating_count
        :type creating_count: int
        :param running_count: running_count
        :type running_count: int
        :param stopping_count: stopping_count
        :type stopping_count: int
        """
        self.allocating_count = self._define_number(
            "allocating_count", allocating_count, ge=0
        )
        self.creating_count = self._define_number(
            "creating_count", creating_count, ge=0
        )
        self.running_count = self._define_number("running_count", running_count, ge=0)
        self.stopping_count = self._define_number(
            "stopping_count", stopping_count, ge=0
        )
