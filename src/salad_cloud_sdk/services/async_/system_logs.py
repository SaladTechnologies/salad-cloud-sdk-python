from typing import Awaitable, Union
from .utils.to_async import to_async
from ..system_logs import SystemLogsService
from ...models import SystemLogList


class SystemLogsServiceAsync(SystemLogsService):
    """
    Async Wrapper for SystemLogsServiceAsync
    """

    def get_system_logs(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Awaitable[SystemLogList]:
        return to_async(super().get_system_logs)(
            organization_name, project_name, container_group_name
        )
