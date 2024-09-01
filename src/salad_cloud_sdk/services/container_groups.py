from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_container_group import UpdateContainerGroup
from ..models.create_container_group import CreateContainerGroup
from ..models.container_group_list import ContainerGroupList
from ..models.container_group_instances import ContainerGroupInstances
from ..models.container_group_instance import ContainerGroupInstance
from ..models.container_group import ContainerGroup


class ContainerGroupsService(BaseService):

    @cast_models
    def list_container_groups(
        self, organization_name: str, project_name: str
    ) -> ContainerGroupList:
        """Gets the list of container groups

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ContainerGroupList
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return ContainerGroupList._unmap(response)

    @cast_models
    def create_container_group(
        self,
        request_body: CreateContainerGroup,
        organization_name: str,
        project_name: str,
    ) -> ContainerGroup:
        """Creates a new container group

        :param request_body: The request body.
        :type request_body: CreateContainerGroup
        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: ContainerGroup
        """

        Validator(CreateContainerGroup).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return ContainerGroup._unmap(response)

    @cast_models
    def get_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> ContainerGroup:
        """Gets a container group

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return ContainerGroup._unmap(response)

    @cast_models
    def update_container_group(
        self,
        request_body: UpdateContainerGroup,
        organization_name: str,
        project_name: str,
        container_group_name: str,
    ) -> ContainerGroup:
        """Updates a container group

        :param request_body: The request body.
        :type request_body: UpdateContainerGroup
        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ContainerGroup
        """

        Validator(UpdateContainerGroup).validate(request_body)
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body, "application/merge-patch+json")
        )

        response = self.send_request(serialized_request)
        return ContainerGroup._unmap(response)

    @cast_models
    def delete_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Any:
        """Deletes a container group

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def start_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Any:
        """Starts a container group

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/start",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def stop_container_group(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> Any:
        """Stops a container group

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/stop",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def list_container_group_instances(
        self, organization_name: str, project_name: str, container_group_name: str
    ) -> ContainerGroupInstances:
        """Retrieves a list of container group instances

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ContainerGroupInstances
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return ContainerGroupInstances._unmap(response)

    @cast_models
    def get_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> ContainerGroupInstance:
        """Retrieves the details of a single instance within a container group by instance ID

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique instance identifier
        :type container_group_instance_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return ContainerGroupInstance._unmap(response)

    @cast_models
    def reallocate_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> Any:
        """Remove a node from a workload and reallocate the workload to a different node

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique instance identifier
        :type container_group_instance_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}/reallocate",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def recreate_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> Any:
        """Stops a container, destroys it, creates a new one without requiring the image to be downloaded again on a different node

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique instance identifier
        :type container_group_instance_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}/recreate",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def restart_container_group_instance(
        self,
        organization_name: str,
        project_name: str,
        container_group_name: str,
        container_group_instance_id: str,
    ) -> Any:
        """Restarts a workload on a node without reallocating it

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param container_group_name: The unique container group name
        :type container_group_name: str
        :param container_group_instance_id: The unique instance identifier
        :type container_group_instance_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/containers/{{container_group_name}}/instances/{{container_group_instance_id}}/restart",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("container_group_name", container_group_name)
            .add_path("container_group_instance_id", container_group_instance_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return response
