from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupTcpProbe(BaseModel):
    """Configuration for a TCP probe used to check container health via network connectivity.

    :param port: The TCP port number that the probe should connect to. Must be a valid port number between 0 and 65535.
    :type port: int
    """

    def __init__(self, port: int, **kwargs):
        """Configuration for a TCP probe used to check container health via network connectivity.

        :param port: The TCP port number that the probe should connect to. Must be a valid port number between 0 and 65535.
        :type port: int
        """
        self.port = self._define_number("port", port, ge=0, le=65535)
        self._kwargs = kwargs
