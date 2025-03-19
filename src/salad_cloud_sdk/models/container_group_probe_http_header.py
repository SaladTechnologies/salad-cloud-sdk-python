from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupProbeHttpHeader(BaseModel):
    """ContainerGroupProbeHttpHeader

    :param name: The name of the HTTP header
    :type name: str
    :param value: The value associated with the HTTP header
    :type value: str
    """

    def __init__(self, name: str, value: str, **kwargs):
        """ContainerGroupProbeHttpHeader

        :param name: The name of the HTTP header
        :type name: str
        :param value: The value associated with the HTTP header
        :type value: str
        """
        self.name = self._define_str(
            "name", name, pattern="^.*$", min_length=1, max_length=256
        )
        self.value = self._define_str(
            "value", value, pattern="^.*$", min_length=1, max_length=1024
        )
        self._kwargs = kwargs
