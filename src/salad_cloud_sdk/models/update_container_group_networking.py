from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class UpdateContainerGroupNetworking(BaseModel):
    """Represents update container group networking parameters

    :param port: port, defaults to None
    :type port: int, optional
    """

    def __init__(self, port: int = None):
        """Represents update container group networking parameters

        :param port: port, defaults to None
        :type port: int, optional
        """
        self.port = self._define_number("port", port, nullable=True, ge=1, le=65535)
