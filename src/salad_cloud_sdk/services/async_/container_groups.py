from typing import Awaitable, Union
from .utils.to_async import to_async
from ..container_groups import ContainerGroupsService
from ...models import (
    ContainerGroupCollection,
    ContainerGroup,
    ContainerGroupCreationRequest,
    ContainerGroupPatch,
    ContainerGroupInstanceCollection,
    ContainerGroupInstance,
    ContainerGroupInstancePatch,
)


class ContainerGroupsServiceAsync(ContainerGroupsService):
    """
    Async Wrapper for ContainerGroupsServiceAsync
    """

    def list_container_groups(
        self, organization_name: str, project_name: str
    ) -> Awaitable[ContainerGroupCollection]:
        return to_async(super().list_container_groups)(organization_name, project_name)

    def create_container_group(
        self,
        request_body: ContainerGroupCreationRequest,
        organization_name: str,
        project_name: str,
    ) -> Awaitable[ContainerGroup]:
        return to_async(super().create_container_group)(
            request_body, organization_name, project_name
        )

    def get_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Awaitable[ContainerGroup]:
        return to_async(super().get_container_group)(
            organization_name, project_name, container_group_name
        )

    def update_container_group(
        self,
        request_body: ContainerGroupPatch,
        organization_name: str,
        project_name: str,
        container_group_name: str,
    ) -> Awaitable[ContainerGroup]:
        return to_async(super().update_container_group)(
            request_body, organization_name, project_name, container_group_name
        )

    def delete_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Awaitable[None]:
        return to_async(super().delete_container_group)(
            organization_name, project_name, container_group_name
        )

    def start_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Awaitable[None]:
        return to_async(super().start_container_group)(
            organization_name, project_name, container_group_name
        )

    def stop_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Awaitable[None]:
        return to_async(super().stop_container_group)(
            organization_name, project_name, container_group_name
        )

    def list_container_group_instances(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Awaitable[ContainerGroupInstanceCollection]:
        return to_async(super().list_container_group_instances)(
            organization_name, project_name, container_group_name
        )

    def get_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> Awaitable[ContainerGroupInstance]:
        return to_async(super().get_container_group_instance)(
            organization_name,
            project_name,
            container_group_name,
            container_group_instance_id,
        )

    def update_container_group_instance(
        self,
        request_body: ContainerGroupInstancePatch,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> Awaitable[ContainerGroupInstance]:
        return to_async(super().update_container_group_instance)(
            request_body,
            organization_name,
            project_name,
            container_group_name,
            container_group_instance_id,
        )

    def reallocate_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> Awaitable[None]:
        return to_async(super().reallocate_container_group_instance)(
            organization_name,
            project_name,
            container_group_name,
            container_group_instance_id,
        )

    def recreate_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> Awaitable[None]:
        return to_async(super().recreate_container_group_instance)(
            organization_name,
            project_name,
            container_group_name,
            container_group_instance_id,
        )

    def restart_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> Awaitable[None]:
        return to_async(super().restart_container_group_instance)(
            organization_name,
            project_name,
            container_group_name,
            container_group_instance_id,
        )
