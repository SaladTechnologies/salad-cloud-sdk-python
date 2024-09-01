from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerResourceRequirements(BaseModel):
    """Represents a container resource requirements

    :param cpu: cpu
    :type cpu: int
    :param memory: memory
    :type memory: int
    :param gpu_classes: gpu_classes, defaults to None
    :type gpu_classes: List[str], optional
    :param storage_amount: storage_amount, defaults to None
    :type storage_amount: int, optional
    """

    def __init__(
        self,
        cpu: int,
        memory: int,
        gpu_classes: List[str] = None,
        storage_amount: int = None,
    ):
        """Represents a container resource requirements

        :param cpu: cpu
        :type cpu: int
        :param memory: memory
        :type memory: int
        :param gpu_classes: gpu_classes, defaults to None
        :type gpu_classes: List[str], optional
        :param storage_amount: storage_amount, defaults to None
        :type storage_amount: int, optional
        """
        self.cpu = self._define_number("cpu", cpu, ge=1, le=16)
        self.memory = self._define_number("memory", memory, ge=1024, le=30720)
        self.gpu_classes = gpu_classes
        self.storage_amount = self._define_number(
            "storage_amount",
            storage_amount,
            nullable=True,
            ge=1073741824,
            le=53687091200,
        )
