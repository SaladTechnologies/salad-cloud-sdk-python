from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"type_": "type"})
class LogEntryResource(BaseModel):
    """The resource associated with the log entry

    :param labels: The labels associated with the resource
    :type labels: dict
    :param type_: The type of the resource
    :type type_: str
    """

    def __init__(self, labels: dict, type_: str, **kwargs):
        """The resource associated with the log entry

        :param labels: The labels associated with the resource
        :type labels: dict
        :param type_: The type of the resource
        :type type_: str
        """
        self.labels = labels
        self.type_ = self._define_str("type_", type_, min_length=1, max_length=1000)
        self._kwargs = kwargs
