from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class TcpLoggingConfiguration(BaseModel):
    """Configuration for forwarding container logs to a remote TCP endpoint

    :param host: The hostname or IP address of the remote TCP logging endpoint
    :type host: str
    :param port: The port number on which the TCP logging endpoint is listening
    :type port: int
    """

    def __init__(self, host: str, port: int, **kwargs):
        """Configuration for forwarding container logs to a remote TCP endpoint

        :param host: The hostname or IP address of the remote TCP logging endpoint
        :type host: str
        :param port: The port number on which the TCP logging endpoint is listening
        :type port: int
        """
        self.host = self._define_str(
            "host", host, pattern="^.*$", min_length=1, max_length=1000
        )
        self.port = self._define_number("port", port, ge=1, le=65535)
        self._kwargs = kwargs
