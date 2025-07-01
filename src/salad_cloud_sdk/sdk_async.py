from typing import Union
from .net.environment import Environment
from .sdk import SaladCloudSdk
from .services.async_.container_groups import ContainerGroupsServiceAsync
from .services.async_.workload_errors import WorkloadErrorsServiceAsync
from .services.async_.system_logs import SystemLogsServiceAsync
from .services.async_.queues import QueuesServiceAsync
from .services.async_.quotas import QuotasServiceAsync
from .services.async_.inference_endpoints import InferenceEndpointsServiceAsync
from .services.async_.organization_data import OrganizationDataServiceAsync
from .services.async_.webhook_secret_key import WebhookSecretKeyServiceAsync
from .services.async_.logs import LogsServiceAsync


class SaladCloudSdkAsync(SaladCloudSdk):
    """
    SaladCloudSdkAsync is the asynchronous version of the SaladCloudSdk SDK Client.
    """

    def __init__(
        self,
        api_key: str = None,
        api_key_header: str = "Salad-Api-Key",
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        super().__init__(
            api_key=api_key,
            api_key_header=api_key_header,
            base_url=base_url,
            timeout=timeout,
        )

        self.container_groups = ContainerGroupsServiceAsync(base_url=self._base_url)
        self.workload_errors = WorkloadErrorsServiceAsync(base_url=self._base_url)
        self.system_logs = SystemLogsServiceAsync(base_url=self._base_url)
        self.queues = QueuesServiceAsync(base_url=self._base_url)
        self.quotas = QuotasServiceAsync(base_url=self._base_url)
        self.inference_endpoints = InferenceEndpointsServiceAsync(
            base_url=self._base_url
        )
        self.organization_data = OrganizationDataServiceAsync(base_url=self._base_url)
        self.webhook_secret_key = WebhookSecretKeyServiceAsync(base_url=self._base_url)
        self.logs = LogsServiceAsync(base_url=self._base_url)
