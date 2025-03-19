from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class QueueBasedAutoscalerConfiguration(BaseModel):
    """Defines configuration for automatically scaling container instances based on queue length. The autoscaler monitors a queue and adjusts the number of running replicas to maintain the desired queue length.

    :param desired_queue_length: The target number of items in the queue that the autoscaler attempts to maintain by scaling the containers up or down
    :type desired_queue_length: int
    :param max_replicas: The maximum number of instances the container can scale up to
    :type max_replicas: int
    :param max_downscale_per_minute: The maximum number of instances that can be removed per minute to prevent rapid downscaling, defaults to None
    :type max_downscale_per_minute: int, optional
    :param max_upscale_per_minute: The maximum number of instances that can be added per minute to prevent rapid upscaling, defaults to None
    :type max_upscale_per_minute: int, optional
    :param min_replicas: The minimum number of instances the container can scale down to, ensuring baseline availability
    :type min_replicas: int
    :param polling_period: The period (in seconds) in which the autoscaler checks the queue length and applies the scaling formula, defaults to None
    :type polling_period: int, optional
    """

    def __init__(
        self,
        desired_queue_length: int,
        max_replicas: int,
        min_replicas: int,
        max_downscale_per_minute: int = SENTINEL,
        max_upscale_per_minute: int = SENTINEL,
        polling_period: int = SENTINEL,
        **kwargs
    ):
        """Defines configuration for automatically scaling container instances based on queue length. The autoscaler monitors a queue and adjusts the number of running replicas to maintain the desired queue length.

        :param desired_queue_length: The target number of items in the queue that the autoscaler attempts to maintain by scaling the containers up or down
        :type desired_queue_length: int
        :param max_replicas: The maximum number of instances the container can scale up to
        :type max_replicas: int
        :param max_downscale_per_minute: The maximum number of instances that can be removed per minute to prevent rapid downscaling, defaults to None
        :type max_downscale_per_minute: int, optional
        :param max_upscale_per_minute: The maximum number of instances that can be added per minute to prevent rapid upscaling, defaults to None
        :type max_upscale_per_minute: int, optional
        :param min_replicas: The minimum number of instances the container can scale down to, ensuring baseline availability
        :type min_replicas: int
        :param polling_period: The period (in seconds) in which the autoscaler checks the queue length and applies the scaling formula, defaults to None
        :type polling_period: int, optional
        """
        self.desired_queue_length = self._define_number(
            "desired_queue_length", desired_queue_length, ge=1, le=100
        )
        self.max_replicas = self._define_number(
            "max_replicas", max_replicas, ge=1, le=500
        )
        if max_downscale_per_minute is not SENTINEL:
            self.max_downscale_per_minute = self._define_number(
                "max_downscale_per_minute", max_downscale_per_minute, ge=1, le=100
            )
        if max_upscale_per_minute is not SENTINEL:
            self.max_upscale_per_minute = self._define_number(
                "max_upscale_per_minute", max_upscale_per_minute, ge=1, le=100
            )
        self.min_replicas = self._define_number(
            "min_replicas", min_replicas, ge=0, le=100
        )
        if polling_period is not SENTINEL:
            self.polling_period = self._define_number(
                "polling_period", polling_period, ge=15, le=1800
            )
        self._kwargs = kwargs
