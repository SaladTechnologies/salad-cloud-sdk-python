from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


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

    def __init__(
        self,
        input: any,
        metadata: Union[dict, None] = SENTINEL,
        webhook: Union[str, None] = SENTINEL,
        **kwargs
    ):
        """Represents a request to create a queue job

        :param input: The job input. May be any valid JSON.
        :type input: any
        :param metadata: metadata, defaults to None
        :type metadata: dict, optional
        :param webhook: webhook, defaults to None
        :type webhook: str, optional
        """
        self.input = input
        if metadata is not SENTINEL:
            self.metadata = metadata
        if webhook is not SENTINEL:
            self.webhook = self._define_str("webhook", webhook, nullable=True)
        self._kwargs = kwargs
