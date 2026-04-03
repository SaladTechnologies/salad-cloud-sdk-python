from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .datadog_tag_for_container_logging import DatadogTagForContainerLogging


@JsonMap({})
class DatadogLoggingConfiguration(BaseModel):
    """Configuration for forwarding container logs to Datadog monitoring service.

    :param api_key: The Datadog API key used for authentication when sending logs.
    :type api_key: str
    :param host: The Datadog intake server host URL where logs will be sent.
    :type host: str
    :param tags: Optional metadata tags to attach to logs for filtering and categorization in Datadog.
    :type tags: List[DatadogTagForContainerLogging]
    """

    def __init__(
        self,
        api_key: str,
        host: str,
        tags: Union[List[DatadogTagForContainerLogging], None],
        **kwargs,
    ):
        """Configuration for forwarding container logs to Datadog monitoring service.

        :param api_key: The Datadog API key used for authentication when sending logs.
        :type api_key: str
        :param host: The Datadog intake server host URL where logs will be sent.
        :type host: str
        :param tags: Optional metadata tags to attach to logs for filtering and categorization in Datadog.
        :type tags: List[DatadogTagForContainerLogging]
        """
        self.api_key = self._define_str(
            "api_key", api_key, pattern="^.*$", min_length=1, max_length=1000
        )
        self.host = self._define_str(
            "host", host, pattern="^.*$", min_length=1, max_length=1000
        )
        self.tags = self._define_list(
            tags, DatadogTagForContainerLogging, nullable=True
        )
        self._kwargs = kwargs
