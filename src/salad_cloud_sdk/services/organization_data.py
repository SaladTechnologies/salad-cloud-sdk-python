from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import GpuClassesList


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
                f"{self.base_url}/organizations/{{organization_name}}/gpu-classes",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return GpuClassesList._unmap(response)
