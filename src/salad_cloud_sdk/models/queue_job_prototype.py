from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class QueueJobPrototype(BaseModel):
    """Represents a request to create a queue job

    :param input: The job input. May be any valid JSON.
    :type input: any
    :param metadata: Additional metadata for the job, defaults to None
    :type metadata: dict, optional
    :param webhook: The webhook to call when the job completes, defaults to None
    :type webhook: str, optional
    """

    def __init__(
        self, input: any, metadata: dict = SENTINEL, webhook: str = SENTINEL, **kwargs
    ):
        """Represents a request to create a queue job

        :param input: The job input. May be any valid JSON.
        :type input: any
        :param metadata: Additional metadata for the job, defaults to None
        :type metadata: dict, optional
        :param webhook: The webhook to call when the job completes, defaults to None
        :type webhook: str, optional
        """
        self.input = input
        if metadata is not SENTINEL:
            self.metadata = metadata
        if webhook is not SENTINEL:
            self.webhook = self._define_str(
                "webhook", webhook, pattern="^.*$", min_length=1, max_length=2048
            )
        self._kwargs = kwargs
