from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class WorkloadError(BaseModel):
    """Represents a workload error

    :param detail: detail
    :type detail: str
    :param failed_at: failed_at
    :type failed_at: str
    :param instance_id: instance_id
    :type instance_id: str
    :param machine_id: machine_id
    :type machine_id: str
    :param allocated_at: allocated_at
    :type allocated_at: str
    :param started_at: started_at, defaults to None
    :type started_at: str, optional
    :param version: version
    :type version: int
    """

    def __init__(
        self,
        detail: str,
        failed_at: str,
        instance_id: str,
        machine_id: str,
        allocated_at: str,
        version: int,
        started_at: str = None,
    ):
        """Represents a workload error

        :param detail: detail
        :type detail: str
        :param failed_at: failed_at
        :type failed_at: str
        :param instance_id: instance_id
        :type instance_id: str
        :param machine_id: machine_id
        :type machine_id: str
        :param allocated_at: allocated_at
        :type allocated_at: str
        :param started_at: started_at, defaults to None
        :type started_at: str, optional
        :param version: version
        :type version: int
        """
        self.detail = detail
        self.failed_at = failed_at
        self.instance_id = instance_id
        self.machine_id = machine_id
        self.allocated_at = allocated_at
        self.started_at = self._define_str("started_at", started_at, nullable=True)
        self.version = self._define_number("version", version, ge=1)
