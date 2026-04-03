from typing import Awaitable, Union
from .utils.to_async import to_async
from ..organizations import OrganizationsService
from ...models import (
    CpuAvailability,
    CpuAvailabilityPrototype,
    GpuAvailability,
    GpuAvailabilityPrototype,
)


class OrganizationsServiceAsync(OrganizationsService):
    """
    Async Wrapper for OrganizationsServiceAsync
    """

    def get_cpu_availability(
        self, request_body: CpuAvailabilityPrototype, organization_name: str
    ) -> Awaitable[CpuAvailability]:
        return to_async(super().get_cpu_availability)(request_body, organization_name)

    def get_gpu_availability(
        self, request_body: GpuAvailabilityPrototype, organization_name: str
    ) -> Awaitable[GpuAvailability]:
        return to_async(super().get_gpu_availability)(request_body, organization_name)
