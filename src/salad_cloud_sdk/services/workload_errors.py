from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import WorkloadErrorList


class WorkloadErrorsService(BaseService):

    @cast_models
    def get_workload_errors(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> WorkloadErrorList:
        """Gets the workload errors

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: WorkloadErrorList
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(container_group_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/errors",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return WorkloadErrorList._unmap(response)
