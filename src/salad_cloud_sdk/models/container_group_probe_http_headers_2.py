from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupProbeHttpHeaders2(BaseModel):
    """ContainerGroupProbeHttpHeaders2

    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str):
        """ContainerGroupProbeHttpHeaders2

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value
