from typing import Awaitable, Union
from .utils.to_async import to_async
from ..organization_data import OrganizationDataService
from ...models import GpuClassesList


class OrganizationDataServiceAsync(OrganizationDataService):
    """
    Async Wrapper for OrganizationDataServiceAsync
    """

    def list_gpu_classes(self, organization_name: str) -> Awaitable[GpuClassesList]:
        return to_async(super().list_gpu_classes)(organization_name)
