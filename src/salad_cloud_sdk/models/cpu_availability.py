from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class CpuAvailability(BaseModel):
    """CpuAvailability

    :param available_cpu_batch: The number of available CPU cores, defaults to None
    :type available_cpu_batch: int, optional
    :param on_call_cpu: The amount of on-call CPU, defaults to None
    :type on_call_cpu: int, optional
    """

    def __init__(
        self, available_cpu_batch: int = SENTINEL, on_call_cpu: int = SENTINEL, **kwargs
    ):
        """CpuAvailability

        :param available_cpu_batch: The number of available CPU cores, defaults to None
        :type available_cpu_batch: int, optional
        :param on_call_cpu: The amount of on-call CPU, defaults to None
        :type on_call_cpu: int, optional
        """
        if available_cpu_batch is not SENTINEL:
            self.available_cpu_batch = available_cpu_batch
        if on_call_cpu is not SENTINEL:
            self.on_call_cpu = on_call_cpu
        self._kwargs = kwargs
