from .services.container_groups import ContainerGroupsService
from .services.workload_errors import WorkloadErrorsService
from .services.queues import QueuesService
from .services.quotas import QuotasService
from .services.inference_endpoints import InferenceEndpointsService
from .services.organization_data import OrganizationDataService
from .services.webhook_secret_key import WebhookSecretKeyService
from .net.environment import Environment


class SaladCloudSdk:
    def __init__(
        self,
        api_key: str = None,
        api_key_header: str = "Salad-Api-Key",
        base_url: str = Environment.DEFAULT.value,
        timeout: int = 60000,
    ):
        """
        Initializes SaladCloudSdk the SDK class.
        """

        self.container_groups = ContainerGroupsService(base_url=base_url)
        self.workload_errors = WorkloadErrorsService(base_url=base_url)
        self.queues = QueuesService(base_url=base_url)
        self.quotas = QuotasService(base_url=base_url)
        self.inference_endpoints = InferenceEndpointsService(base_url=base_url)
        self.organization_data = OrganizationDataService(base_url=base_url)
        self.webhook_secret_key = WebhookSecretKeyService(base_url=base_url)
        self.set_api_key(api_key, api_key_header)
        self.set_timeout(timeout)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.container_groups.set_base_url(base_url)
        self.workload_errors.set_base_url(base_url)
        self.queues.set_base_url(base_url)
        self.quotas.set_base_url(base_url)
        self.inference_endpoints.set_base_url(base_url)
        self.organization_data.set_base_url(base_url)
        self.webhook_secret_key.set_base_url(base_url)

        return self

    def set_api_key(self, api_key: str, api_key_header="Salad-Api-Key"):
        """
        Sets the api key and the api key header for the entire SDK.
        """
        self.container_groups.set_api_key(api_key, api_key_header)
        self.workload_errors.set_api_key(api_key, api_key_header)
        self.queues.set_api_key(api_key, api_key_header)
        self.quotas.set_api_key(api_key, api_key_header)
        self.inference_endpoints.set_api_key(api_key, api_key_header)
        self.organization_data.set_api_key(api_key, api_key_header)
        self.webhook_secret_key.set_api_key(api_key, api_key_header)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.container_groups.set_timeout(timeout)
        self.workload_errors.set_timeout(timeout)
        self.queues.set_timeout(timeout)
        self.quotas.set_timeout(timeout)
        self.inference_endpoints.set_timeout(timeout)
        self.organization_data.set_timeout(timeout)
        self.webhook_secret_key.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
