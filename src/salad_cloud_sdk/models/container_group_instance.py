from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class State(Enum):
    """An enumeration representing different categories.

    :cvar ALLOCATING: "allocating"
    :vartype ALLOCATING: str
    :cvar DOWNLOADING: "downloading"
    :vartype DOWNLOADING: str
    :cvar CREATING: "creating"
    :vartype CREATING: str
    :cvar RUNNING: "running"
    :vartype RUNNING: str
    :cvar STOPPING: "stopping"
    :vartype STOPPING: str
    """

    ALLOCATING = "allocating"
    DOWNLOADING = "downloading"
    CREATING = "creating"
    RUNNING = "running"
    STOPPING = "stopping"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, State._member_map_.values()))


@JsonMap({})
class ContainerGroupInstance(BaseModel):
    """Represents the details of a single container group instance

    :param instance_id: The unique instance ID
    :type instance_id: str
    :param machine_id: The machine ID
    :type machine_id: str
    :param state: The state of the container group instance
    :type state: State
    :param update_time: The UTC date & time when the workload on this machine transitioned to the current state
    :type update_time: str
    :param version: The version of the running container group
    :type version: int
    :param ready: Specifies whether the container group instance is currently passing its readiness check. If no readiness probe is defined, is true once fully started., defaults to None
    :type ready: bool, optional
    :param started: Specifies whether the container group instance passed its startup probe. Is always true when no startup probe is defined., defaults to None
    :type started: bool, optional
    """

    def __init__(
        self,
        instance_id: str,
        machine_id: str,
        state: State,
        update_time: str,
        version: int,
        ready: bool = None,
        started: bool = None,
    ):
        """Represents the details of a single container group instance

        :param instance_id: The unique instance ID
        :type instance_id: str
        :param machine_id: The machine ID
        :type machine_id: str
        :param state: The state of the container group instance
        :type state: State
        :param update_time: The UTC date & time when the workload on this machine transitioned to the current state
        :type update_time: str
        :param version: The version of the running container group
        :type version: int
        :param ready: Specifies whether the container group instance is currently passing its readiness check. If no readiness probe is defined, is true once fully started., defaults to None
        :type ready: bool, optional
        :param started: Specifies whether the container group instance passed its startup probe. Is always true when no startup probe is defined., defaults to None
        :type started: bool, optional
        """
        self.instance_id = instance_id
        self.machine_id = machine_id
        self.state = self._enum_matching(state, State.list(), "state")
        self.update_time = update_time
        self.version = self._define_number("version", version, ge=1)
        self.ready = ready
        self.started = started
