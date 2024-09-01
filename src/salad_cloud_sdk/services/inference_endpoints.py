from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.inference_endpoints_list import InferenceEndpointsList
from ..models.inference_endpoint_job_list import InferenceEndpointJobList
from ..models.inference_endpoint_job import InferenceEndpointJob
from ..models.inference_endpoint import InferenceEndpoint
from ..models.create_inference_endpoint_job import CreateInferenceEndpointJob


class InferenceEndpointsService(BaseService):

    @cast_models
    def list_inference_endpoints(
        self, organization_name: str, page: int = None, page_size: int = None
    ) -> InferenceEndpointsList:
        """Gets the list of all inference endpoints

        :param organization_name: The unique organization name
        :type organization_name: str
        :param page: The page number, defaults to None
        :type page: int, optional
        :param page_size: The number of items per page, defaults to None
        :type page_size: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: InferenceEndpointsList
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(int).is_optional().min(1).max(2147483647).validate(page)
        Validator(int).is_optional().min(1).max(100).validate(page_size)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/inference-endpoints",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_query("page", page, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InferenceEndpointsList._unmap(response)

    @cast_models
    def get_inference_endpoint(
        self, organization_name: str, inference_endpoint_name: str
    ) -> InferenceEndpoint:
        """Gets an inference endpoint

        :param organization_name: The unique organization name
        :type organization_name: str
        :param inference_endpoint_name: The unique inference endpoint name
        :type inference_endpoint_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: InferenceEndpoint
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).validate(inference_endpoint_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InferenceEndpoint._unmap(response)

    @cast_models
    def get_inference_endpoint_jobs(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        page: int = None,
        page_size: int = None,
    ) -> InferenceEndpointJobList:
        """Retrieves a list of an inference endpoint jobs

        :param organization_name: The unique organization name
        :type organization_name: str
        :param inference_endpoint_name: The unique inference endpoint name
        :type inference_endpoint_name: str
        :param page: The page number, defaults to None
        :type page: int, optional
        :param page_size: The number of items per page, defaults to None
        :type page_size: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: InferenceEndpointJobList
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).validate(inference_endpoint_name)
        Validator(int).is_optional().min(1).max(2147483647).validate(page)
        Validator(int).is_optional().min(1).max(100).validate(page_size)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}/jobs",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .add_query("page", page, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InferenceEndpointJobList._unmap(response)

    @cast_models
    def create_inference_endpoint_job(
        self,
        request_body: CreateInferenceEndpointJob,
        organization_name: str,
        inference_endpoint_name: str,
    ) -> InferenceEndpointJob:
        """Creates a new job

        :param request_body: The request body.
        :type request_body: CreateInferenceEndpointJob
        :param organization_name: The unique organization name
        :type organization_name: str
        :param inference_endpoint_name: The unique inference endpoint name
        :type inference_endpoint_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: InferenceEndpointJob
        """

        Validator(CreateInferenceEndpointJob).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).validate(inference_endpoint_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}/jobs",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InferenceEndpointJob._unmap(response)

    @cast_models
    def get_inference_endpoint_job(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        inference_endpoint_job_id: str,
    ) -> InferenceEndpointJob:
        """Retrieves a job in an inference endpoint

        :param organization_name: The unique organization name
        :type organization_name: str
        :param inference_endpoint_name: The unique inference endpoint name
        :type inference_endpoint_name: str
        :param inference_endpoint_job_id: The unique job id
        :type inference_endpoint_job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Ok
        :rtype: InferenceEndpointJob
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).validate(inference_endpoint_name)
        Validator(str).validate(inference_endpoint_job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}/jobs/{{inference_endpoint_job_id}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .add_path("inference_endpoint_job_id", inference_endpoint_job_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InferenceEndpointJob._unmap(response)

    @cast_models
    def delete_inference_endpoint_job(
        self,
        organization_name: str,
        inference_endpoint_name: str,
        inference_endpoint_job_id: str,
    ) -> Any:
        """Deletes an inference endpoint job

        :param organization_name: The unique organization name
        :type organization_name: str
        :param inference_endpoint_name: The unique inference endpoint name
        :type inference_endpoint_name: str
        :param inference_endpoint_job_id: The unique job id
        :type inference_endpoint_job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).validate(inference_endpoint_name)
        Validator(str).validate(inference_endpoint_job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/inference-endpoints/{{inference_endpoint_name}}/jobs/{{inference_endpoint_job_id}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("inference_endpoint_name", inference_endpoint_name)
            .add_path("inference_endpoint_job_id", inference_endpoint_job_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return response
