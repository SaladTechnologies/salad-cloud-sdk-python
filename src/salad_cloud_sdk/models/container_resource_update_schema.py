from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class ContainerResourceUpdateSchema(BaseModel):
    """Defines the resource specifications that can be modified for a container group, including CPU, memory, GPU classes, and storage allocations.

    :param cpu: The number of CPU cores to allocate to the container (between 1 and 16 cores)., defaults to None
    :type cpu: int, optional
    :param memory: The amount of memory to allocate to the container in megabytes (between 1024MB and 61440MB)., defaults to None
    :type memory: int, optional
    :param gpu_classes: List of GPU class identifiers that the container can use, specified as UUIDs., defaults to None
    :type gpu_classes: List[str], optional
    :param storage_amount: The amount of storage to allocate to the container in bytes (between 1GB and 250GB)., defaults to None
    :type storage_amount: int, optional
    :param shm_size: The size of the shared memory (/dev/shm) in MB. If not specified, defaults to 64MB., defaults to None
    :type shm_size: int, optional
    """

    def __init__(
        self,
        cpu: Union[int, None] = SENTINEL,
        memory: Union[int, None] = SENTINEL,
        gpu_classes: Union[List[str], None] = SENTINEL,
        storage_amount: Union[int, None] = SENTINEL,
        shm_size: Union[int, None] = SENTINEL,
        **kwargs
    ):
        """Defines the resource specifications that can be modified for a container group, including CPU, memory, GPU classes, and storage allocations.

        :param cpu: The number of CPU cores to allocate to the container (between 1 and 16 cores)., defaults to None
        :type cpu: int, optional
        :param memory: The amount of memory to allocate to the container in megabytes (between 1024MB and 61440MB)., defaults to None
        :type memory: int, optional
        :param gpu_classes: List of GPU class identifiers that the container can use, specified as UUIDs., defaults to None
        :type gpu_classes: List[str], optional
        :param storage_amount: The amount of storage to allocate to the container in bytes (between 1GB and 250GB)., defaults to None
        :type storage_amount: int, optional
        :param shm_size: The size of the shared memory (/dev/shm) in MB. If not specified, defaults to 64MB., defaults to None
        :type shm_size: int, optional
        """
        if cpu is not SENTINEL:
            self.cpu = self._define_number("cpu", cpu, nullable=True, ge=1, le=16)
        if memory is not SENTINEL:
            self.memory = self._define_number(
                "memory", memory, nullable=True, ge=1024, le=61440
            )
        if gpu_classes is not SENTINEL:
            self.gpu_classes = gpu_classes
        if storage_amount is not SENTINEL:
            self.storage_amount = self._define_number(
                "storage_amount",
                storage_amount,
                nullable=True,
                ge=1073741824,
                le=268435456000,
            )
        if shm_size is not SENTINEL:
            self.shm_size = self._define_number(
                "shm_size", shm_size, nullable=True, ge=64, le=2147483647
            )
        self._kwargs = kwargs
