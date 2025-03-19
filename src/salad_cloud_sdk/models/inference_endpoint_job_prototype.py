from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class InferenceEndpointJobPrototype(BaseModel):
    """Represents a request to create a inference endpoint job

    :param input: The job input. May be any valid JSON.
    :type input: any
    :param metadata: The job metadata. May be any valid JSON., defaults to None
    :type metadata: dict, optional
    :param webhook: The webhook URL to which the job results will be POSTed., defaults to None
    :type webhook: str, optional
    :param webhook_url: The webhook URL to which the job results will be POSTed., defaults to None
    :type webhook_url: str, optional
    """

    def __init__(
        self,
        input: any,
        metadata: dict = SENTINEL,
        webhook: str = SENTINEL,
        webhook_url: str = SENTINEL,
        **kwargs
    ):
        """Represents a request to create a inference endpoint job

        :param input: The job input. May be any valid JSON.
        :type input: any
        :param metadata: The job metadata. May be any valid JSON., defaults to None
        :type metadata: dict, optional
        :param webhook: The webhook URL to which the job results will be POSTed., defaults to None
        :type webhook: str, optional
        :param webhook_url: The webhook URL to which the job results will be POSTed., defaults to None
        :type webhook_url: str, optional
        """
        self.input = input
        if metadata is not SENTINEL:
            self.metadata = metadata
        if webhook is not SENTINEL:
            self.webhook = self._define_str(
                "webhook", webhook, min_length=1, max_length=2048
            )
        if webhook_url is not SENTINEL:
            self.webhook_url = self._define_str(
                "webhook_url", webhook_url, min_length=1, max_length=2048
            )
        self._kwargs = kwargs
