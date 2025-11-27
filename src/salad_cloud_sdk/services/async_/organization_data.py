from typing import Awaitable, Union
from .utils.to_async import to_async
from ..organization_data import OrganizationDataService
from ...models import (
    GpuClassesList,
    CpuAvailability,
    CpuAvailabilityPrototype,
    GpuAvailability,
    GpuAvailabilityPrototype,
)


class OrganizationDataServiceAsync(OrganizationDataService):
    """
    Async Wrapper for OrganizationDataServiceAsync
    """

    def list_gpu_classes(self, organization_name: str) -> Awaitable[GpuClassesList]:
        return to_async(super().list_gpu_classes)(organization_name)

    def get_cpu_availability(
        self, request_body: CpuAvailabilityPrototype, organization_name: str
    ) -> Awaitable[CpuAvailability]:
        return to_async(super().get_cpu_availability)(request_body, organization_name)

    def get_gpu_availability(
        self, request_body: GpuAvailabilityPrototype, organization_name: str
    ) -> Awaitable[GpuAvailability]:
        return to_async(super().get_gpu_availability)(request_body, organization_name)
