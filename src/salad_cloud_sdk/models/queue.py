from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group import ContainerGroup


@JsonMap({"id_": "id"})
class Queue(BaseModel):
    """Represents a queue

    :param id_: id_
    :type id_: str
    :param name: name
    :type name: str
    :param display_name: display_name
    :type display_name: str
    :param description: The description, defaults to None
    :type description: str, optional
    :param container_groups: container_groups
    :type container_groups: List[ContainerGroup]
    :param create_time: create_time
    :type create_time: str
    :param update_time: update_time
    :type update_time: str
    """

    def __init__(
        self,
        id_: str,
        name: str,
        display_name: str,
        container_groups: List[ContainerGroup],
        create_time: str,
        update_time: str,
        description: str = None,
    ):
        """Represents a queue

        :param id_: id_
        :type id_: str
        :param name: name
        :type name: str
        :param display_name: display_name
        :type display_name: str
        :param description: The description, defaults to None
        :type description: str, optional
        :param container_groups: container_groups
        :type container_groups: List[ContainerGroup]
        :param create_time: create_time
        :type create_time: str
        :param update_time: update_time
        :type update_time: str
        """
        self.id_ = id_
        self.name = self._define_str(
            "name",
            name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.display_name = self._define_str(
            "display_name",
            display_name,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.description = self._define_str(
            "description", description, nullable=True, max_length=500
        )
        self.container_groups = self._define_list(container_groups, ContainerGroup)
        self.create_time = create_time
        self.update_time = update_time
