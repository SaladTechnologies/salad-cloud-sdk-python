from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupGRpcProbe(BaseModel):
    """Configuration for gRPC-based health probes in container groups, used to determine container health status.

    :param port: The port number on which the gRPC health check service is exposed.
    :type port: int
    :param service: The name of the gRPC service that implements the health check protocol.
    :type service: str
    """

    def __init__(self, port: int, service: str, **kwargs):
        """Configuration for gRPC-based health probes in container groups, used to determine container health status.

        :param port: The port number on which the gRPC health check service is exposed.
        :type port: int
        :param service: The name of the gRPC service that implements the health check protocol.
        :type service: str
        """
        self.port = self._define_number("port", port, ge=0, le=65536)
        self.service = self._define_str(
            "service", service, pattern="^.*$", max_length=1024
        )
        self._kwargs = kwargs
