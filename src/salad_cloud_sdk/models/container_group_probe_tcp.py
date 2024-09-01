from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupProbeTcp(BaseModel):
    """ContainerGroupProbeTcp

    :param port: port
    :type port: int
    """

    def __init__(self, port: int):
        """ContainerGroupProbeTcp

        :param port: port
        :type port: int
        """
        self.port = self._define_number("port", port, ge=0, le=65536)
