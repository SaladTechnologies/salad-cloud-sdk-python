from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupProbeExec(BaseModel):
    """Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks.

    :param command: The command to execute inside the container. Exit status of 0 is considered successful, any other exit status is considered failure.
    :type command: List[str]
    """

    def __init__(self, command: List[str], **kwargs):
        """Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks.

        :param command: The command to execute inside the container. Exit status of 0 is considered successful, any other exit status is considered failure.
        :type command: List[str]
        """
        self.command = command
        self._kwargs = kwargs
