from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerGroupScalingAction(BaseModel):
    """Represents a scaling action configuration for a container group

    :param replicas: The number of replicas to scale to during the scheduled period
    :type replicas: int
    :param schedule: The cron-style schedule string defining when the scaling should occur
    :type schedule: str
    """

    def __init__(self, replicas: int, schedule: str, **kwargs):
        """Represents a scaling action configuration for a container group

        :param replicas: The number of replicas to scale to during the scheduled period
        :type replicas: int
        :param schedule: The cron-style schedule string defining when the scaling should occur
        :type schedule: str
        """
        self.replicas = self._define_number("replicas", replicas, ge=0, le=500)
        self.schedule = self._define_str(
            "schedule",
            schedule,
            pattern="^([0-9A-Za-z*/,-]+)([\t ]+[0-9A-Za-z*/,-]+){4}$",
        )
        self._kwargs = kwargs
