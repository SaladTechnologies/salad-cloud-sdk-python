from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class AxiomLoggingConfiguration(BaseModel):
    """Configuration settings for integrating container logs with the Axiom logging service. When specified, container logs will be forwarded to the Axiom instance defined by these parameters.

    :param api_token: Authentication token for the Axiom API with appropriate write permissions
    :type api_token: str
    :param dataset: Name of the Axiom dataset where the container logs will be stored and indexed
    :type dataset: str
    :param host: The Axiom host URL where logs will be sent (e.g. logs.axiom.co)
    :type host: str
    """

    def __init__(self, api_token: str, dataset: str, host: str, **kwargs):
        """Configuration settings for integrating container logs with the Axiom logging service. When specified, container logs will be forwarded to the Axiom instance defined by these parameters.

        :param api_token: Authentication token for the Axiom API with appropriate write permissions
        :type api_token: str
        :param dataset: Name of the Axiom dataset where the container logs will be stored and indexed
        :type dataset: str
        :param host: The Axiom host URL where logs will be sent (e.g. logs.axiom.co)
        :type host: str
        """
        self.api_token = self._define_str(
            "api_token", api_token, pattern="^.*$", min_length=1, max_length=1000
        )
        self.dataset = self._define_str(
            "dataset", dataset, pattern="^.*$", min_length=1, max_length=1000
        )
        self.host = self._define_str(
            "host", host, pattern="^.*$", min_length=1, max_length=1000
        )
        self._kwargs = kwargs
