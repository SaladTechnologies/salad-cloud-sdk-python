from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class ContainerResourceRequirements(BaseModel):
    """Specifies the resource requirements for a container.

    :param cpu: The number of CPU cores required by the container. Must be between 1 and 16.
    :type cpu: int
    :param memory: The amount of memory (in MB) required by the container. Must be between 1024 MB and 61440 MB.
    :type memory: int
    :param gpu_classes: A list of GPU class UUIDs required by the container. Can be null if no GPU is required.
    :type gpu_classes: List[str]
    :param storage_amount: The amount of storage (in bytes) required by the container. Must be between 1 GB (1073741824 bytes) and 250 GB (268435456000 bytes)., defaults to None
    :type storage_amount: int, optional
    :param shm_size: The size of the shared memory (/dev/shm) in MB. If not specified, defaults to 64MB., defaults to None
    :type shm_size: int, optional
    """

    def __init__(
        self,
        cpu: int,
        memory: int,
        gpu_classes: List[str],
        storage_amount: int = SENTINEL,
        shm_size: int = SENTINEL,
        **kwargs
    ):
        """Specifies the resource requirements for a container.

        :param cpu: The number of CPU cores required by the container. Must be between 1 and 16.
        :type cpu: int
        :param memory: The amount of memory (in MB) required by the container. Must be between 1024 MB and 61440 MB.
        :type memory: int
        :param gpu_classes: A list of GPU class UUIDs required by the container. Can be null if no GPU is required.
        :type gpu_classes: List[str]
        :param storage_amount: The amount of storage (in bytes) required by the container. Must be between 1 GB (1073741824 bytes) and 250 GB (268435456000 bytes)., defaults to None
        :type storage_amount: int, optional
        :param shm_size: The size of the shared memory (/dev/shm) in MB. If not specified, defaults to 64MB., defaults to None
        :type shm_size: int, optional
        """
        self.cpu = self._define_number("cpu", cpu, ge=1, le=16)
        self.memory = self._define_number("memory", memory, ge=1024, le=61440)
        self.gpu_classes = gpu_classes
        if storage_amount is not SENTINEL:
            self.storage_amount = self._define_number(
                "storage_amount", storage_amount, ge=1073741824, le=268435456000
            )
        if shm_size is not SENTINEL:
            self.shm_size = self._define_number(
                "shm_size", shm_size, ge=64, le=2147483647
            )
        self._kwargs = kwargs
