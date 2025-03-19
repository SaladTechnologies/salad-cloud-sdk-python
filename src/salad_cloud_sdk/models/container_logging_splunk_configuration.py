from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerLoggingSplunkConfiguration(BaseModel):
    """Configuration settings for forwarding container logs to a Splunk instance.

    :param host: The URL of the Splunk HTTP Event Collector (HEC) endpoint.
    :type host: str
    :param token: The authentication token required to send data to the Splunk HEC endpoint.
    :type token: str
    """

    def __init__(self, host: str, token: str, **kwargs):
        """Configuration settings for forwarding container logs to a Splunk instance.

        :param host: The URL of the Splunk HTTP Event Collector (HEC) endpoint.
        :type host: str
        :param token: The authentication token required to send data to the Splunk HEC endpoint.
        :type token: str
        """
        self.host = self._define_str(
            "host", host, pattern="^.*$", min_length=1, max_length=1000
        )
        self.token = self._define_str(
            "token", token, pattern="^.*$", min_length=1, max_length=1000
        )
        self._kwargs = kwargs
