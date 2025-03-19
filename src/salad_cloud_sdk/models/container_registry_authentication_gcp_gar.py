from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerRegistryAuthenticationGcpGar(BaseModel):
    """Authentication details for Google Artifact Registry (GAR)

    :param service_key: GCP service account key in JSON format for GAR authentication
    :type service_key: str
    """

    def __init__(self, service_key: str, **kwargs):
        """Authentication details for Google Artifact Registry (GAR)

        :param service_key: GCP service account key in JSON format for GAR authentication
        :type service_key: str
        """
        self.service_key = self._define_str(
            "service_key", service_key, pattern="^.*$", min_length=1, max_length=1000
        )
        self._kwargs = kwargs
