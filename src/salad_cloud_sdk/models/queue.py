from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_group import ContainerGroup


@JsonMap({"id_": "id"})
class Queue(BaseModel):
    """Represents a queue.

    :param container_groups: The container groups that are part of this queue. Each container group represents a scalable set of identical containers running as a distributed service.
    :type container_groups: List[ContainerGroup]
    :param create_time: The date and time the queue was created.
    :type create_time: str
    :param current_queue_length: The current length of the queue, defaults to None
    :type current_queue_length: int, optional
    :param description: The description. This may be used as a space for notes or other information about the queue., defaults to None
    :type description: str, optional
    :param display_name: The display name. This may be used as a more human-readable name.
    :type display_name: str
    :param id_: The queue identifier. This is automatically generated and assigned when the queue is created.
    :type id_: str
    :param name: The queue name. This must be unique within the project.
    :type name: str
    :param update_time: The date and time the queue was last updated.
    :type update_time: str
    """

    def __init__(
        self,
        container_groups: List[ContainerGroup],
        create_time: str,
        display_name: str,
        id_: str,
        name: str,
        update_time: str,
        current_queue_length: int = SENTINEL,
        description: str = SENTINEL,
        **kwargs,
    ):
        """Represents a queue.

        :param container_groups: The container groups that are part of this queue. Each container group represents a scalable set of identical containers running as a distributed service.
        :type container_groups: List[ContainerGroup]
        :param create_time: The date and time the queue was created.
        :type create_time: str
        :param current_queue_length: The current length of the queue, defaults to None
        :type current_queue_length: int, optional
        :param description: The description. This may be used as a space for notes or other information about the queue., defaults to None
        :type description: str, optional
        :param display_name: The display name. This may be used as a more human-readable name.
        :type display_name: str
        :param id_: The queue identifier. This is automatically generated and assigned when the queue is created.
        :type id_: str
        :param name: The queue name. This must be unique within the project.
        :type name: str
        :param update_time: The date and time the queue was last updated.
        :type update_time: str
        """
        self.container_groups = self._define_list(container_groups, ContainerGroup)
        self.create_time = self._define_str("create_time", create_time)
        if current_queue_length is not SENTINEL:
            self.current_queue_length = self._define_number(
                "current_queue_length", current_queue_length, ge=0, le=2147483647
            )
        if description is not SENTINEL:
            self.description = self._define_str(
                "description", description, pattern="^.*$", max_length=500
            )
        self.display_name = self._define_str(
            "display_name",
            display_name,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.id_ = self._define_str("id_", id_)
        self.name = self._define_str(
            "name",
            name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.update_time = self._define_str("update_time", update_time)
        self._kwargs = kwargs
