from __future__ import annotations
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_group_instance_status_count import ContainerGroupInstanceStatusCount
from .container_group_status import ContainerGroupStatus


@JsonMap({})
class ContainerGroupState(BaseModel):
    """Represents the operational state of a container group during its lifecycle, including timing information, status, and instance distribution metrics. This state captures the current execution status, start and finish times, and provides visibility into the operational health across instances.

    :param description: Optional textual description or notes about the current state of the container group, defaults to None
    :type description: str, optional
    :param finish_time: Timestamp when the container group execution finished or is expected to finish
    :type finish_time: str
    :param instance_status_counts: A summary of container group instances categorized by their current lifecycle status
    :type instance_status_counts: ContainerGroupInstanceStatusCount
    :param start_time: Timestamp when the container group execution started
    :type start_time: str
    :param status: Represents the current operational state of a container group within the Salad platform.
    :type status: ContainerGroupStatus
    """

    def __init__(
        self,
        finish_time: str,
        instance_status_counts: ContainerGroupInstanceStatusCount,
        start_time: str,
        status: ContainerGroupStatus,
        description: Union[str, None] = SENTINEL,
        **kwargs,
    ):
        """Represents the operational state of a container group during its lifecycle, including timing information, status, and instance distribution metrics. This state captures the current execution status, start and finish times, and provides visibility into the operational health across instances.

        :param description: Optional textual description or notes about the current state of the container group, defaults to None
        :type description: str, optional
        :param finish_time: Timestamp when the container group execution finished or is expected to finish
        :type finish_time: str
        :param instance_status_counts: A summary of container group instances categorized by their current lifecycle status
        :type instance_status_counts: ContainerGroupInstanceStatusCount
        :param start_time: Timestamp when the container group execution started
        :type start_time: str
        :param status: Represents the current operational state of a container group within the Salad platform.
        :type status: ContainerGroupStatus
        """
        if description is not SENTINEL:
            self.description = self._define_str(
                "description",
                description,
                nullable=True,
                pattern="^.*$",
                max_length=1000,
            )
        self.finish_time = finish_time
        self.instance_status_counts = self._define_object(
            instance_status_counts, ContainerGroupInstanceStatusCount
        )
        self.start_time = start_time
        self.status = self._enum_matching(status, ContainerGroupStatus.list(), "status")
        self._kwargs = kwargs
