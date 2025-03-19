from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupQueueConnection(BaseModel):
    """Configuration for connecting a container group to a message queue system, enabling asynchronous communication between services.

    :param path: The endpoint path for accessing the queue service, relative to the base URL of the queue server.
    :type path: str
    :param port: The network port number used to connect to the queue service. Must be a valid TCP/IP port between 1 and 65535.
    :type port: int
    :param queue_name: Unique identifier for the queue. Must start with a lowercase letter, can contain lowercase letters, numbers, and hyphens, and must end with a letter or number.
    :type queue_name: str
    """

    def __init__(self, path: str, port: int, queue_name: str, **kwargs):
        """Configuration for connecting a container group to a message queue system, enabling asynchronous communication between services.

        :param path: The endpoint path for accessing the queue service, relative to the base URL of the queue server.
        :type path: str
        :param port: The network port number used to connect to the queue service. Must be a valid TCP/IP port between 1 and 65535.
        :type port: int
        :param queue_name: Unique identifier for the queue. Must start with a lowercase letter, can contain lowercase letters, numbers, and hyphens, and must end with a letter or number.
        :type queue_name: str
        """
        self.path = self._define_str(
            "path", path, pattern="^.*$", min_length=1, max_length=1024
        )
        self.port = self._define_number("port", port, ge=1, le=65535)
        self.queue_name = self._define_str(
            "queue_name",
            queue_name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self._kwargs = kwargs
