from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group_status import ContainerGroupStatus
from .container_group_instance_status_count import ContainerGroupInstanceStatusCount


@JsonMap({})
class ContainerGroupState(BaseModel):
    """Represents a container group state

    :param status: status
    :type status: ContainerGroupStatus
    :param description: description, defaults to None
    :type description: str, optional
    :param start_time: start_time
    :type start_time: str
    :param finish_time: finish_time
    :type finish_time: str
    :param instance_status_counts: Represents a container group instance status count
    :type instance_status_counts: ContainerGroupInstanceStatusCount
    """

    def __init__(
        self,
        status: ContainerGroupStatus,
        start_time: str,
        finish_time: str,
        instance_status_counts: ContainerGroupInstanceStatusCount,
        description: str = None,
    ):
        """Represents a container group state

        :param status: status
        :type status: ContainerGroupStatus
        :param description: description, defaults to None
        :type description: str, optional
        :param start_time: start_time
        :type start_time: str
        :param finish_time: finish_time
        :type finish_time: str
        :param instance_status_counts: Represents a container group instance status count
        :type instance_status_counts: ContainerGroupInstanceStatusCount
        """
        self.status = self._enum_matching(status, ContainerGroupStatus.list(), "status")
        self.description = self._define_str("description", description, nullable=True)
        self.start_time = start_time
        self.finish_time = finish_time
        self.instance_status_counts = self._define_object(
            instance_status_counts, ContainerGroupInstanceStatusCount
        )
