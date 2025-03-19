from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class UpdateContainerGroupNetworking(BaseModel):
    """Represents update container group networking parameters

    :param port: The port number to expose on the container group, defaults to None
    :type port: int, optional
    """

    def __init__(self, port: Union[int, None] = SENTINEL, **kwargs):
        """Represents update container group networking parameters

        :param port: The port number to expose on the container group, defaults to None
        :type port: int, optional
        """
        if port is not SENTINEL:
            self.port = self._define_number("port", port, nullable=True, ge=1, le=65535)
        self._kwargs = kwargs
