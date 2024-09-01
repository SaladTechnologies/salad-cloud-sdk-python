from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class UpdateQueue(BaseModel):
    """Represents a request to update a queue

    :param display_name: display_name, defaults to None
    :type display_name: str, optional
    :param description: The description, defaults to None
    :type description: str, optional
    """

    def __init__(self, display_name: str = None, description: str = None):
        """Represents a request to update a queue

        :param display_name: display_name, defaults to None
        :type display_name: str, optional
        :param description: The description, defaults to None
        :type description: str, optional
        """
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
