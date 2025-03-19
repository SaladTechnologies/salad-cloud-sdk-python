from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupInstanceStatusCount(BaseModel):
    """A summary of container group instances categorized by their current lifecycle status

    :param allocating_count: The number of container instances that are currently being allocated resources
    :type allocating_count: int
    :param creating_count: The number of container instances that are in the process of being created
    :type creating_count: int
    :param running_count: The number of container instances that are currently running and operational
    :type running_count: int
    :param stopping_count: The number of container instances that are in the process of stopping
    :type stopping_count: int
    """

    def __init__(
        self,
        allocating_count: int,
        creating_count: int,
        running_count: int,
        stopping_count: int,
        **kwargs
    ):
        """A summary of container group instances categorized by their current lifecycle status

        :param allocating_count: The number of container instances that are currently being allocated resources
        :type allocating_count: int
        :param creating_count: The number of container instances that are in the process of being created
        :type creating_count: int
        :param running_count: The number of container instances that are currently running and operational
        :type running_count: int
        :param stopping_count: The number of container instances that are in the process of stopping
        :type stopping_count: int
        """
        self.allocating_count = self._define_number(
            "allocating_count", allocating_count, ge=0, le=2147483647
        )
        self.creating_count = self._define_number(
            "creating_count", creating_count, ge=0, le=2147483647
        )
        self.running_count = self._define_number(
            "running_count", running_count, ge=0, le=2147483647
        )
        self.stopping_count = self._define_number(
            "stopping_count", stopping_count, ge=0, le=2147483647
        )
        self._kwargs = kwargs
