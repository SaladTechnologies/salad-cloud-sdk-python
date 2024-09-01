from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupProbeExec(BaseModel):
    """ContainerGroupProbeExec

    :param command: command
    :type command: List[str]
    """

    def __init__(self, command: List[str]):
        """ContainerGroupProbeExec

        :param command: command
        :type command: List[str]
        """
        self.command = command
