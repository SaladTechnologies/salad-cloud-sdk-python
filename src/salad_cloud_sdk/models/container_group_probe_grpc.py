from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupProbeGrpc(BaseModel):
    """ContainerGroupProbeGrpc

    :param service: service
    :type service: str
    :param port: port
    :type port: int
    """

    def __init__(self, service: str, port: int):
        """ContainerGroupProbeGrpc

        :param service: service
        :type service: str
        :param port: port
        :type port: int
        """
        self.service = service
        self.port = self._define_number("port", port, ge=0, le=65536)
