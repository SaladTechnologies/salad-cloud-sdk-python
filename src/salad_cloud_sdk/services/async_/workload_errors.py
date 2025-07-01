from typing import Awaitable, Union
from .utils.to_async import to_async
from ..workload_errors import WorkloadErrorsService
from ...models import WorkloadErrorList


class WorkloadErrorsServiceAsync(WorkloadErrorsService):
    """
    Async Wrapper for WorkloadErrorsServiceAsync
    """

    def get_workload_errors(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Awaitable[WorkloadErrorList]:
        return to_async(super().get_workload_errors)(
            organization_name, project_name, container_group_name
        )
