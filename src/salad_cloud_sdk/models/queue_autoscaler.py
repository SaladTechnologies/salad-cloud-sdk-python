from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class QueueAutoscaler(BaseModel):
    """Represents the autoscaling rules for a queue

    :param min_replicas: The minimum number of instances the container can scale down to
    :type min_replicas: int
    :param max_replicas: The maximum number of instances the container can scale up to
    :type max_replicas: int
    :param desired_queue_length: desired_queue_length
    :type desired_queue_length: int
    :param polling_period: The period (in seconds) in which the queue checks the formula, defaults to None
    :type polling_period: int, optional
    :param max_upscale_per_minute: The maximum number of instances that can be added per minute, defaults to None
    :type max_upscale_per_minute: int, optional
    :param max_downscale_per_minute: The maximum number of instances that can be removed per minute, defaults to None
    :type max_downscale_per_minute: int, optional
    """

    def __init__(
        self,
        min_replicas: int,
        max_replicas: int,
        desired_queue_length: int,
        polling_period: int = SENTINEL,
        max_upscale_per_minute: int = SENTINEL,
        max_downscale_per_minute: int = SENTINEL,
        **kwargs
    ):
        """Represents the autoscaling rules for a queue

        :param min_replicas: The minimum number of instances the container can scale down to
        :type min_replicas: int
        :param max_replicas: The maximum number of instances the container can scale up to
        :type max_replicas: int
        :param desired_queue_length: desired_queue_length
        :type desired_queue_length: int
        :param polling_period: The period (in seconds) in which the queue checks the formula, defaults to None
        :type polling_period: int, optional
        :param max_upscale_per_minute: The maximum number of instances that can be added per minute, defaults to None
        :type max_upscale_per_minute: int, optional
        :param max_downscale_per_minute: The maximum number of instances that can be removed per minute, defaults to None
        :type max_downscale_per_minute: int, optional
        """
        self.min_replicas = self._define_number(
            "min_replicas", min_replicas, ge=0, le=100
        )
        self.max_replicas = self._define_number(
            "max_replicas", max_replicas, ge=1, le=500
        )
        self.desired_queue_length = self._define_number(
            "desired_queue_length", desired_queue_length, ge=1, le=100
        )
        if polling_period is not SENTINEL:
            self.polling_period = self._define_number(
                "polling_period", polling_period, ge=15, le=1800
            )
        if max_upscale_per_minute is not SENTINEL:
            self.max_upscale_per_minute = self._define_number(
                "max_upscale_per_minute", max_upscale_per_minute, ge=1, le=100
            )
        if max_downscale_per_minute is not SENTINEL:
            self.max_downscale_per_minute = self._define_number(
                "max_downscale_per_minute", max_downscale_per_minute, ge=1, le=100
            )
        self._kwargs = kwargs
