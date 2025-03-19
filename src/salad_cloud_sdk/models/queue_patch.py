from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class QueuePatch(BaseModel):
    """Represents a request to update an existing queue.

    :param display_name: The display name. This may be used as a more human-readable name., defaults to None
    :type display_name: str, optional
    :param description: The description. This may be used as a space for notes or other information about the queue., defaults to None
    :type description: str, optional
    """

    def __init__(
        self,
        display_name: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        **kwargs
    ):
        """Represents a request to update an existing queue.

        :param display_name: The display name. This may be used as a more human-readable name., defaults to None
        :type display_name: str, optional
        :param description: The description. This may be used as a space for notes or other information about the queue., defaults to None
        :type description: str, optional
        """
        if display_name is not SENTINEL:
            self.display_name = self._define_str(
                "display_name",
                display_name,
                nullable=True,
                pattern="^[ ,-.0-9A-Za-z]+$",
                min_length=2,
                max_length=63,
            )
        if description is not SENTINEL:
            self.description = self._define_str(
                "description",
                description,
                nullable=True,
                pattern="^.*$",
                max_length=500,
            )
        self._kwargs = kwargs
