from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class WorkloadError(BaseModel):
    """Represents a workload error

    :param allocated_at: The timestamp when the workload was initially allocated to a machine
    :type allocated_at: str
    :param detail: A detailed error message describing the nature and cause of the workload failure
    :type detail: str
    :param failed_at: The timestamp when the workload failure was detected or reported
    :type failed_at: str
    :param instance_id: The container group instance identifier.
    :type instance_id: str
    :param machine_id: The container group machine identifier.
    :type machine_id: str
    :param started_at: The timestamp when the workload started execution, or null if it failed before starting, defaults to None
    :type started_at: str, optional
    :param version: The schema version number for this error record, used for tracking error format changes
    :type version: int
    """

    def __init__(
        self,
        allocated_at: str,
        detail: str,
        failed_at: str,
        instance_id: str,
        machine_id: str,
        version: int,
        started_at: str = SENTINEL,
        **kwargs
    ):
        """Represents a workload error

        :param allocated_at: The timestamp when the workload was initially allocated to a machine
        :type allocated_at: str
        :param detail: A detailed error message describing the nature and cause of the workload failure
        :type detail: str
        :param failed_at: The timestamp when the workload failure was detected or reported
        :type failed_at: str
        :param instance_id: The container group instance identifier.
        :type instance_id: str
        :param machine_id: The container group machine identifier.
        :type machine_id: str
        :param started_at: The timestamp when the workload started execution, or null if it failed before starting, defaults to None
        :type started_at: str, optional
        :param version: The schema version number for this error record, used for tracking error format changes
        :type version: int
        """
        self.allocated_at = allocated_at
        self.detail = self._define_str(
            "detail", detail, pattern="^.*$", min_length=1, max_length=255
        )
        self.failed_at = failed_at
        self.instance_id = instance_id
        self.machine_id = machine_id
        if started_at is not SENTINEL:
            self.started_at = started_at
        self.version = self._define_number("version", version, ge=1, le=2147483647)
        self._kwargs = kwargs
