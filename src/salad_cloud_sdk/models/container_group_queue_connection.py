from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupQueueConnection(BaseModel):
    """Represents container group queue connection

    :param path: path
    :type path: str
    :param port: port
    :type port: int
    :param queue_name: queue_name
    :type queue_name: str
    """

    def __init__(self, path: str, port: int, queue_name: str):
        """Represents container group queue connection

        :param path: path
        :type path: str
        :param port: port
        :type port: int
        :param queue_name: queue_name
        :type queue_name: str
        """
        self.path = self._define_str("path", path, min_length=1, max_length=1024)
        self.port = self._define_number("port", port, ge=1, le=65535)
        self.queue_name = self._define_str(
            "queue_name",
            queue_name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
