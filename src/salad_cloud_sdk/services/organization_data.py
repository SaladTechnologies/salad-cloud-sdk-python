from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    CpuAvailability,
    CpuAvailabilityPrototype,
    GpuAvailability,
    GpuAvailabilityPrototype,
    GpuClassesList,
    ProblemDetails,
)


class OrganizationDataService(BaseService):

    @cast_models
    def list_gpu_classes(self, organization_name: str) -> GpuClassesList:
        """List the GPU Classes

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GpuClassesList
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/gpu-classes",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return GpuClassesList._unmap(response)

    @cast_models
    def get_cpu_availability(
        self, request_body: CpuAvailabilityPrototype, organization_name: str
    ) -> CpuAvailability:
        """Gets the CPU availability for the given organization

        :param request_body: The request body.
        :type request_body: CpuAvailabilityPrototype
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: CpuAvailability
        """

        Validator(CpuAvailabilityPrototype).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/availability/sce-cpu-availability",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
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
        return CpuAvailability._unmap(response)

    @cast_models
    def get_gpu_availability(
        self, request_body: GpuAvailabilityPrototype, organization_name: str
    ) -> GpuAvailability:
        """Gets the GPU availability for the given organization

        :param request_body: The request body.
        :type request_body: GpuAvailabilityPrototype
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GpuAvailability
        """

        Validator(GpuAvailabilityPrototype).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/availability/sce-gpu-availability",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
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
        return GpuAvailability._unmap(response)
