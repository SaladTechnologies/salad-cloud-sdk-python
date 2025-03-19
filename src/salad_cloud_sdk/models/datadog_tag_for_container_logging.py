from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class DatadogTagForContainerLogging(BaseModel):
    """Represents a Datadog tag used for container logging metadata.

    :param name: The name of the metadata tag.
    :type name: str
    :param value: The value of the metadata tag.
    :type value: str
    """

    def __init__(self, name: str, value: str, **kwargs):
        """Represents a Datadog tag used for container logging metadata.

        :param name: The name of the metadata tag.
        :type name: str
        :param value: The value of the metadata tag.
        :type value: str
        """
        self.name = self._define_str(
            "name", name, pattern="^.*$", min_length=1, max_length=1000
        )
        self.value = self._define_str(
            "value", value, pattern="^.*$", min_length=1, max_length=1000
        )
        self._kwargs = kwargs
