from typing import Awaitable, Union
from .utils.to_async import to_async
from ..inference_endpoints import InferenceEndpointsService
from ...models.utils.sentinel import SENTINEL
from ...models import (
    InferenceEndpointCollection,
    InferenceEndpoint,
    InferenceEndpointJobCollection,
    InferenceEndpointJob,
    InferenceEndpointJobPrototype,
)


class InferenceEndpointsServiceAsync(InferenceEndpointsService):
    """
    Async Wrapper for InferenceEndpointsServiceAsync
    """

    def list_inference_endpoints(
        self, organization_name: str, page: int = SENTINEL, page_size: int = SENTINEL
    ) -> Awaitable[InferenceEndpointCollection]:
        return to_async(super().list_inference_endpoints)(
            organization_name, page, page_size
        )

    def get_inference_endpoint(
        self, organization_name: str, inference_endpoint_name: str
    ) -> Awaitable[InferenceEndpoint]:
        return to_async(super().get_inference_endpoint)(
            organization_name, inference_endpoint_name
        )

    def list_inference_endpoint_jobs(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        page: int = SENTINEL,
        page_size: int = SENTINEL,
    ) -> Awaitable[InferenceEndpointJobCollection]:
        return to_async(super().list_inference_endpoint_jobs)(
            organization_name, inference_endpoint_name, page, page_size
        )

    def create_inference_endpoint_job(
        self,
        request_body: InferenceEndpointJobPrototype,
        organization_name: str,
        inference_endpoint_name: str,
    ) -> Awaitable[InferenceEndpointJob]:
        return to_async(super().create_inference_endpoint_job)(
            request_body, organization_name, inference_endpoint_name
        )

    def get_inference_endpoint_job(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        inference_endpoint_job_id: str,
    ) -> Awaitable[InferenceEndpointJob]:
        return to_async(super().get_inference_endpoint_job)(
            organization_name, inference_endpoint_name, inference_endpoint_job_id
        )

    def delete_inference_endpoint_job(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        inference_endpoint_job_id: str,
    ) -> Awaitable[None]:
        return to_async(super().delete_inference_endpoint_job)(
            organization_name, inference_endpoint_name, inference_endpoint_job_id
        )
