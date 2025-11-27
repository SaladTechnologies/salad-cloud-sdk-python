from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class GpuAvailability(BaseModel):
    """GpuAvailability

    :param available_gpu_batch: The number of available GPU batches, defaults to None
    :type available_gpu_batch: int, optional
    :param available_gpu_low: The number of available low-end GPUs, defaults to None
    :type available_gpu_low: int, optional
    :param available_gpu_medium: The number of available medium-end GPUs, defaults to None
    :type available_gpu_medium: int, optional
    :param available_gpu_high: The number of available high-end GPUs, defaults to None
    :type available_gpu_high: int, optional
    :param on_call_gpu: The number of on-call GPUs available, defaults to None
    :type on_call_gpu: int, optional
    """

    def __init__(
        self,
        available_gpu_batch: int = SENTINEL,
        available_gpu_low: int = SENTINEL,
        available_gpu_medium: int = SENTINEL,
        available_gpu_high: int = SENTINEL,
        on_call_gpu: int = SENTINEL,
        **kwargs
    ):
        """GpuAvailability

        :param available_gpu_batch: The number of available GPU batches, defaults to None
        :type available_gpu_batch: int, optional
        :param available_gpu_low: The number of available low-end GPUs, defaults to None
        :type available_gpu_low: int, optional
        :param available_gpu_medium: The number of available medium-end GPUs, defaults to None
        :type available_gpu_medium: int, optional
        :param available_gpu_high: The number of available high-end GPUs, defaults to None
        :type available_gpu_high: int, optional
        :param on_call_gpu: The number of on-call GPUs available, defaults to None
        :type on_call_gpu: int, optional
        """
        if available_gpu_batch is not SENTINEL:
            self.available_gpu_batch = available_gpu_batch
        if available_gpu_low is not SENTINEL:
            self.available_gpu_low = available_gpu_low
        if available_gpu_medium is not SENTINEL:
            self.available_gpu_medium = available_gpu_medium
        if available_gpu_high is not SENTINEL:
            self.available_gpu_high = available_gpu_high
        if on_call_gpu is not SENTINEL:
            self.on_call_gpu = on_call_gpu
        self._kwargs = kwargs
