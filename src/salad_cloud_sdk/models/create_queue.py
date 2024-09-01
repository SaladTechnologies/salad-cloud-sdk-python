from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateQueue(BaseModel):
    """Represents a request to create a queue

    :param name: name
    :type name: str
    :param display_name: display_name, defaults to None
    :type display_name: str, optional
    :param description: The description, defaults to None
    :type description: str, optional
    """

    def __init__(self, name: str, display_name: str = None, description: str = None):
        """Represents a request to create a queue

        :param name: name
        :type name: str
        :param display_name: display_name, defaults to None
        :type display_name: str, optional
        :param description: The description, defaults to None
        :type description: str, optional
        """
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
            nullable=True,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.description = self._define_str(
            "description", description, nullable=True, max_length=500
        )
