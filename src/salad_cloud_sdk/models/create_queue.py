from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateQueue(BaseModel):
    """Represents a request to create a new queue.

    :param name: The queue name. This must be unique within the project.
    :type name: str
    :param display_name: The display name. This may be used as a more human-readable name., defaults to None
    :type display_name: str, optional
    :param description: The description. This may be used as a space for notes or other information about the queue., defaults to None
    :type description: str, optional
    """

    def __init__(self, name: str, display_name: str = None, description: str = None):
        """Represents a request to create a new queue.

        :param name: The queue name. This must be unique within the project.
        :type name: str
        :param display_name: The display name. This may be used as a more human-readable name., defaults to None
        :type display_name: str, optional
        :param description: The description. This may be used as a space for notes or other information about the queue., defaults to None
        :type description: str, optional
        """
        self.name = self._define_str(
            "name",
            name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        if display_name is not None:
            self.display_name = self._define_str(
                "display_name",
                display_name,
                nullable=True,
                pattern="^[ ,-.0-9A-Za-z]+$",
                min_length=2,
                max_length=63,
            )
        if description is not None:
            self.description = self._define_str(
                "description", description, nullable=True, max_length=500
            )
