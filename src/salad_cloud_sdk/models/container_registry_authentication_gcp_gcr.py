from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerRegistryAuthenticationGcpGcr(BaseModel):
    """Authentication details for Google Container Registry (GCR)

    :param service_key: GCP service account key in JSON format for GCR authentication
    :type service_key: str
    """

    def __init__(self, service_key: str, **kwargs):
        """Authentication details for Google Container Registry (GCR)

        :param service_key: GCP service account key in JSON format for GCR authentication
        :type service_key: str
        """
        self.service_key = self._define_str(
            "service_key", service_key, pattern="^.*$", min_length=1, max_length=1000
        )
        self._kwargs = kwargs
