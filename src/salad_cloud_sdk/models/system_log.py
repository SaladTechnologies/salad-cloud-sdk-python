from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class SystemLog(BaseModel):
    """Represents a system log

    :param event_name: The name of the event
    :type event_name: str
    :param event_time: The UTC date & time when the log item was created
    :type event_time: str
    :param instance_id: The container group instance identifier., defaults to None
    :type instance_id: str, optional
    :param machine_id: The container group machine identifier., defaults to None
    :type machine_id: str, optional
    :param resource_cpu: The number of CPUs
    :type resource_cpu: int
    :param resource_gpu_class: The GPU class name
    :type resource_gpu_class: str
    :param resource_memory: The memory amount in MB
    :type resource_memory: int
    :param resource_storage_amount: The storage amount in bytes
    :type resource_storage_amount: int
    :param version: The version instance ID
    :type version: str
    """

    def __init__(
        self,
        event_name: str,
        event_time: str,
        resource_cpu: Union[int, None],
        resource_gpu_class: str,
        resource_memory: Union[int, None],
        resource_storage_amount: Union[int, None],
        version: str,
        instance_id: str = SENTINEL,
        machine_id: str = SENTINEL,
        **kwargs
    ):
        """Represents a system log

        :param event_name: The name of the event
        :type event_name: str
        :param event_time: The UTC date & time when the log item was created
        :type event_time: str
        :param instance_id: The container group instance identifier., defaults to None
        :type instance_id: str, optional
        :param machine_id: The container group machine identifier., defaults to None
        :type machine_id: str, optional
        :param resource_cpu: The number of CPUs
        :type resource_cpu: int
        :param resource_gpu_class: The GPU class name
        :type resource_gpu_class: str
        :param resource_memory: The memory amount in MB
        :type resource_memory: int
        :param resource_storage_amount: The storage amount in bytes
        :type resource_storage_amount: int
        :param version: The version instance ID
        :type version: str
        """
        self.event_name = self._define_str(
            "event_name", event_name, pattern="^.*$", min_length=1, max_length=255
        )
        self.event_time = event_time
        if instance_id is not SENTINEL:
            self.instance_id = instance_id
        if machine_id is not SENTINEL:
            self.machine_id = machine_id
        self.resource_cpu = self._define_number(
            "resource_cpu", resource_cpu, nullable=True, ge=1, le=16
        )
        self.resource_gpu_class = resource_gpu_class
        self.resource_memory = self._define_number(
            "resource_memory", resource_memory, nullable=True, ge=1024, le=61440
        )
        self.resource_storage_amount = self._define_number(
            "resource_storage_amount",
            resource_storage_amount,
            nullable=True,
            ge=1073741824,
            le=268435456000,
        )
        self.version = version
        self._kwargs = kwargs
