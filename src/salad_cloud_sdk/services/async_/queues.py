from typing import Awaitable, Union
from .utils.to_async import to_async
from ..queues import QueuesService
from ...models.utils.sentinel import SENTINEL
from ...models import (
    QueueCollection,
    Queue,
    QueuePrototype,
    QueuePatch,
    QueueJobCollection,
    QueueJob,
    QueueJobPrototype,
)


class QueuesServiceAsync(QueuesService):
    """
    Async Wrapper for QueuesServiceAsync
    """

    def list_queues(
        self, organization_name: str, project_name: str
    ) -> Awaitable[QueueCollection]:
        return to_async(super().list_queues)(organization_name, project_name)

    def create_queue(
        self, request_body: QueuePrototype, organization_name: str, project_name: str
    ) -> Awaitable[Queue]:
        return to_async(super().create_queue)(
            request_body, organization_name, project_name
        )

    def get_queue(
        self, organization_name: str, project_name: str, queue_name: str
    ) -> Awaitable[Queue]:
        return to_async(super().get_queue)(organization_name, project_name, queue_name)

    def update_queue(
        self,
        request_body: QueuePatch,
        organization_name: str,
        project_name: str,
        queue_name: str,
    ) -> Awaitable[Queue]:
        return to_async(super().update_queue)(
            request_body, organization_name, project_name, queue_name
        )

    def delete_queue(
        self, organization_name: str, project_name: str, queue_name: str
    ) -> Awaitable[None]:
        return to_async(super().delete_queue)(
            organization_name, project_name, queue_name
        )

    def list_queue_jobs(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        page: int = SENTINEL,
        page_size: int = SENTINEL,
    ) -> Awaitable[QueueJobCollection]:
        return to_async(super().list_queue_jobs)(
            organization_name, project_name, queue_name, page, page_size
        )

    def create_queue_job(
        self,
        request_body: QueueJobPrototype,
        organization_name: str,
        project_name: str,
        queue_name: str,
    ) -> Awaitable[QueueJob]:
        return to_async(super().create_queue_job)(
            request_body, organization_name, project_name, queue_name
        )

    def get_queue_job(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        queue_job_id: str,
    ) -> Awaitable[QueueJob]:
        return to_async(super().get_queue_job)(
            organization_name, project_name, queue_name, queue_job_id
        )

    def delete_queue_job(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        queue_job_id: str,
    ) -> Awaitable[None]:
        return to_async(super().delete_queue_job)(
            organization_name, project_name, queue_name, queue_job_id
        )
