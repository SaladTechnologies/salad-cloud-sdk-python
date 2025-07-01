from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    InferenceEndpoint,
    InferenceEndpointCollection,
    InferenceEndpointJob,
    InferenceEndpointJobCollection,
    InferenceEndpointJobPrototype,
    ProblemDetails,
)


class InferenceEndpointsService(BaseService):

    @cast_models
    def list_inference_endpoints(
        self, organization_name: str, page: int = SENTINEL, page_size: int = SENTINEL
    ) -> InferenceEndpointCollection:
        """Lists inference endpoints.

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param page: The page number., defaults to None
        :type page: int, optional
        :param page_size: The maximum number of items per page., defaults to None
        :type page_size: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: InferenceEndpointCollection
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(int).is_optional().min(1).max(2147483647).validate(page)
        Validator(int).is_optional().min(1).max(100).validate(page_size)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/inference-endpoints",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_query("page", page)
            .add_query("page_size", page_size)
            .add_error(400, ProblemDetails)
            .add_error(401, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return InferenceEndpointCollection._unmap(response)

    @cast_models
    def get_inference_endpoint(
        self, organization_name: str, inference_endpoint_name: str
    ) -> InferenceEndpoint:
        """Gets an inference endpoint.

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param inference_endpoint_name: The inference endpoint name.
        :type inference_endpoint_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: InferenceEndpoint
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(inference_endpoint_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .add_error(401, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return InferenceEndpoint._unmap(response)

    @cast_models
    def list_inference_endpoint_jobs(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        page: int = SENTINEL,
        page_size: int = SENTINEL,
    ) -> InferenceEndpointJobCollection:
        """Lists inference endpoint jobs.

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param inference_endpoint_name: The inference endpoint name.
        :type inference_endpoint_name: str
        :param page: The page number., defaults to None
        :type page: int, optional
        :param page_size: The maximum number of items per page., defaults to None
        :type page_size: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: InferenceEndpointJobCollection
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(inference_endpoint_name)
        Validator(int).is_optional().min(1).max(2147483647).validate(page)
        Validator(int).is_optional().min(1).max(100).validate(page_size)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}/jobs",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .add_query("page", page)
            .add_query("page_size", page_size)
            .add_error(400, ProblemDetails)
            .add_error(401, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return InferenceEndpointJobCollection._unmap(response)

    @cast_models
    def create_inference_endpoint_job(
        self,
        request_body: InferenceEndpointJobPrototype,
        organization_name: str,
        inference_endpoint_name: str,
    ) -> InferenceEndpointJob:
        """Creates a new inference endpoint job.

        :param request_body: The request body.
        :type request_body: InferenceEndpointJobPrototype
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param inference_endpoint_name: The inference endpoint name.
        :type inference_endpoint_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: InferenceEndpointJob
        """

        Validator(InferenceEndpointJobPrototype).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(inference_endpoint_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}/jobs",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .add_error(400, ProblemDetails)
            .add_error(401, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return InferenceEndpointJob._unmap(response)

    @cast_models
    def get_inference_endpoint_job(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        inference_endpoint_job_id: str,
    ) -> InferenceEndpointJob:
        """Gets an inference endpoint job.

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param inference_endpoint_name: The inference endpoint name.
        :type inference_endpoint_name: str
        :param inference_endpoint_job_id: The inference endpoint job identifier.
        :type inference_endpoint_job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: InferenceEndpointJob
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(inference_endpoint_name)
        Validator(str).validate(inference_endpoint_job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}/jobs/{{inference_endpoint_job_id}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .add_path("inference_endpoint_job_id", inference_endpoint_job_id)
            .add_error(401, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return InferenceEndpointJob._unmap(response)

    @cast_models
    def delete_inference_endpoint_job(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        inference_endpoint_job_id: str,
    ) -> None:
        """Cancels an inference endpoint job.

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param inference_endpoint_name: The inference endpoint name.
        :type inference_endpoint_name: str
        :param inference_endpoint_job_id: The inference endpoint job identifier.
        :type inference_endpoint_job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: None
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(inference_endpoint_name)
        Validator(str).validate(inference_endpoint_job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}/jobs/{{inference_endpoint_job_id}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .add_path("inference_endpoint_job_id", inference_endpoint_job_id)
            .add_error(400, ProblemDetails)
            .add_error(401, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)
