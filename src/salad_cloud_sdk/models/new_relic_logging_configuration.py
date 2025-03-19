from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class NewRelicLoggingConfiguration(BaseModel):
    """Configuration for sending container logs to New Relic's log management platform.

    :param host: The New Relic endpoint host for log ingestion (e.g., log-api.newrelic.com).
    :type host: str
    :param ingestion_key: The New Relic license or ingestion key used for authentication and data routing.
    :type ingestion_key: str
    """

    def __init__(self, host: str, ingestion_key: str, **kwargs):
        """Configuration for sending container logs to New Relic's log management platform.

        :param host: The New Relic endpoint host for log ingestion (e.g., log-api.newrelic.com).
        :type host: str
        :param ingestion_key: The New Relic license or ingestion key used for authentication and data routing.
        :type ingestion_key: str
        """
        self.host = self._define_str(
            "host", host, pattern="^.*$", min_length=1, max_length=1000
        )
        self.ingestion_key = self._define_str(
            "ingestion_key",
            ingestion_key,
            pattern="^.*$",
            min_length=1,
            max_length=1000,
        )
        self._kwargs = kwargs
