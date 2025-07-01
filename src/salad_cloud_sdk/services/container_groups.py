from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    ContainerGroup,
    ContainerGroupCollection,
    ContainerGroupCreationRequest,
    ContainerGroupInstance,
    ContainerGroupInstanceCollection,
    ContainerGroupInstancePatch,
    ContainerGroupPatch,
    ProblemDetails,
)


class ContainerGroupsService(BaseService):

    @cast_models
    def list_container_groups(
        self, organization_name: str, project_name: str
    ) -> ContainerGroupCollection:
        """Gets the list of container groups

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ContainerGroupCollection
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return ContainerGroupCollection._unmap(response)

    @cast_models
    def create_container_group(
        self,
        request_body: ContainerGroupCreationRequest,
        organization_name: str,
        project_name: str,
    ) -> ContainerGroup:
        """Creates a new container group

        :param request_body: The request body.
        :type request_body: ContainerGroupCreationRequest
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ContainerGroup
        """

        Validator(ContainerGroupCreationRequest).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_error(400, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return ContainerGroup._unmap(response)

    @cast_models
    def get_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> ContainerGroup:
        """Gets a container group

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ContainerGroup
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
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return ContainerGroup._unmap(response)

    @cast_models
    def update_container_group(
        self,
        request_body: ContainerGroupPatch,
        organization_name: str,
        project_name: str,
        container_group_name: str,
    ) -> ContainerGroup:
        """Updates a container group

        :param request_body: The request body.
        :type request_body: ContainerGroupPatch
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ContainerGroup
        """

        Validator(ContainerGroupPatch).validate(request_body)
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
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_error(400, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body, "application/merge-patch+json")
        )

        response, status, content = self.send_request(serialized_request)
        return ContainerGroup._unmap(response)

    @cast_models
    def delete_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> None:
        """Deletes a container group

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
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
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(container_group_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def start_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> None:
        """Starts a container group

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
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
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(container_group_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/start",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_error(400, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def stop_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> None:
        """Stops a container group

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
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
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(container_group_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/stop",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_error(400, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def list_container_group_instances(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> ContainerGroupInstanceCollection:
        """Gets the list of container group instances

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ContainerGroupInstanceCollection
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
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return ContainerGroupInstanceCollection._unmap(response)

    @cast_models
    def get_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> ContainerGroupInstance:
        """Gets a container group instance

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique container group instance identifier
        :type container_group_instance_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ContainerGroupInstance
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
        Validator(str).validate(container_group_instance_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return ContainerGroupInstance._unmap(response)

    @cast_models
    def update_container_group_instance(
        self,
        request_body: ContainerGroupInstancePatch,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> ContainerGroupInstance:
        """Updates a container group instance

        :param request_body: The request body.
        :type request_body: ContainerGroupInstancePatch
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique container group instance identifier
        :type container_group_instance_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ContainerGroupInstance
        """

        Validator(ContainerGroupInstancePatch).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(container_group_name)
        Validator(str).validate(container_group_instance_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .add_error(400, ProblemDetails)
            .add_error(403, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body, "application/merge-patch+json")
        )

        response, status, _ = self.send_request(serialized_request)
        return ContainerGroupInstance._unmap(response)

    @cast_models
    def reallocate_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> None:
        """Reallocates a container group instance to run on a different Salad Node

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique container group instance identifier
        :type container_group_instance_id: str
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
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(container_group_name)
        Validator(str).validate(container_group_instance_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}/reallocate",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def recreate_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> None:
        """Stops a container, destroys it, and starts a new one without requiring the image to be downloaded again on a new Salad Node

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique container group instance identifier
        :type container_group_instance_id: str
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
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(container_group_name)
        Validator(str).validate(container_group_instance_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}/recreate",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def restart_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> None:
        """Stops a container and restarts it on the same Salad Node

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique container group instance identifier
        :type container_group_instance_id: str
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
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(container_group_name)
        Validator(str).validate(container_group_instance_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}/restart",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
        )

        response, status, content = self.send_request(serialized_request)
