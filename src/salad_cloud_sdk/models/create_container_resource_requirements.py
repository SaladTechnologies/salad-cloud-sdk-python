from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class CreateContainerResourceRequirements(BaseModel):
    """Specifies the resource requirements for creating a container.

    :param cpu: The number of CPU cores to allocate to the container (between 1 and 1024).
    :type cpu: int
    :param gpu_classes: A list of GPU class UUIDs required by the container. Can be null if no GPU is required., defaults to None
    :type gpu_classes: List[str], optional
    :param memory: The amount of memory to allocate to the container in megabytes (between 1024 and 1073741824).
    :type memory: int
    :param shm_size: The amount of shared memory to allocate to the container via `/dev/shm` in megabytes (between 64 and 1073741824). If not specified, defaults to 64 MB., defaults to None
    :type shm_size: int, optional
    :param storage_amount: The amount of storage to allocate to the container in bytes (between 1 GB and 1 PB)., defaults to None
    :type storage_amount: int, optional
    """

    def __init__(
        self,
        cpu: int,
        memory: int,
        gpu_classes: List[str] = SENTINEL,
        shm_size: int = SENTINEL,
        storage_amount: int = SENTINEL,
        **kwargs
    ):
        """Specifies the resource requirements for creating a container.

        :param cpu: The number of CPU cores to allocate to the container (between 1 and 1024).
        :type cpu: int
        :param gpu_classes: A list of GPU class UUIDs required by the container. Can be null if no GPU is required., defaults to None
        :type gpu_classes: List[str], optional
        :param memory: The amount of memory to allocate to the container in megabytes (between 1024 and 1073741824).
        :type memory: int
        :param shm_size: The amount of shared memory to allocate to the container via `/dev/shm` in megabytes (between 64 and 1073741824). If not specified, defaults to 64 MB., defaults to None
        :type shm_size: int, optional
        :param storage_amount: The amount of storage to allocate to the container in bytes (between 1 GB and 1 PB)., defaults to None
        :type storage_amount: int, optional
        """
        self.cpu = self._define_number("cpu", cpu, ge=1, le=1024)
        if gpu_classes is not SENTINEL:
            self.gpu_classes = gpu_classes
        self.memory = self._define_number("memory", memory, ge=1024, le=1073741824)
        if shm_size is not SENTINEL:
            self.shm_size = self._define_number(
                "shm_size", shm_size, ge=64, le=1073741824
            )
        if storage_amount is not SENTINEL:
            self.storage_amount = self._define_number(
                "storage_amount", storage_amount, ge=1073741824, le=1125899906842624
            )
        self._kwargs = kwargs
