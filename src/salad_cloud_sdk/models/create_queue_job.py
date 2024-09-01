from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateQueueJob(BaseModel):
    """Represents a request to create a queue job

    :param input: The job input. May be any valid JSON.
    :type input: any
    :param metadata: metadata, defaults to None
    :type metadata: dict, optional
    :param webhook: webhook, defaults to None
    :type webhook: str, optional
    """

    def __init__(self, input: any, metadata: dict = None, webhook: str = None):
        """Represents a request to create a queue job

        :param input: The job input. May be any valid JSON.
        :type input: any
        :param metadata: metadata, defaults to None
        :type metadata: dict, optional
        :param webhook: webhook, defaults to None
        :type webhook: str, optional
        """
        self.input = input
        self.metadata = metadata
        self.webhook = self._define_str("webhook", webhook, nullable=True)
