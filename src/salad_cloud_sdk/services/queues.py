from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    ProblemDetails,
    Queue,
    QueueCollection,
    QueueJob,
    QueueJobCollection,
    QueueJobPrototype,
    QueuePatch,
    QueuePrototype,
)


class QueuesService(BaseService):

    @cast_models
    def list_queues(self, organization_name: str, project_name: str) -> QueueCollection:
        """Gets the list of queues in the given project.

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: QueueCollection
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return QueueCollection._unmap(response)

    @cast_models
    def create_queue(
        self, request_body: QueuePrototype, organization_name: str, project_name: str
    ) -> Queue:
        """Creates a new queue in the given project.

        :param request_body: The request body.
        :type request_body: QueuePrototype
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Queue
        """

        Validator(QueuePrototype).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_error(400, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return Queue._unmap(response)

    @cast_models
    def get_queue(
        self, organization_name: str, project_name: str, queue_name: str
    ) -> Queue:
        """Gets an existing queue in the given project.

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param queue_name: The queue name.
        :type queue_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Queue
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(queue_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return Queue._unmap(response)

    @cast_models
    def update_queue(
        self,
        request_body: QueuePatch,
        organization_name: str,
        project_name: str,
        queue_name: str,
    ) -> Queue:
        """Updates an existing queue in the given project.

        :param request_body: The request body.
        :type request_body: QueuePatch
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param queue_name: The queue name.
        :type queue_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Queue
        """

        Validator(QueuePatch).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(queue_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_error(400, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body, "application/merge-patch+json")
        )

        response, status, _ = self.send_request(serialized_request)
        return Queue._unmap(response)

    @cast_models
    def delete_queue(
        self, organization_name: str, project_name: str, queue_name: str
    ) -> None:
        """Deletes an existing queue in the given project.

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param queue_name: The queue name.
        :type queue_name: str
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
        ).validate(queue_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def list_queue_jobs(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        page: int = SENTINEL,
        page_size: int = SENTINEL,
    ) -> QueueJobCollection:
        """Gets the list of jobs in a queue

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param queue_name: The queue name.
        :type queue_name: str
        :param page: The page number., defaults to None
        :type page: int, optional
        :param page_size: The maximum number of items per page., defaults to None
        :type page_size: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: QueueJobCollection
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(queue_name)
        Validator(int).is_optional().min(1).max(2147483647).validate(page)
        Validator(int).is_optional().min(1).max(100).validate(page_size)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}/jobs",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_query("page", page)
            .add_query("page_size", page_size)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return QueueJobCollection._unmap(response)

    @cast_models
    def create_queue_job(
        self,
        request_body: QueueJobPrototype,
        organization_name: str,
        project_name: str,
        queue_name: str,
    ) -> QueueJob:
        """Creates a new job

        :param request_body: The request body.
        :type request_body: QueueJobPrototype
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param queue_name: The queue name.
        :type queue_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: QueueJob
        """

        Validator(QueueJobPrototype).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(queue_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}/jobs",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_error(400, ProblemDetails)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return QueueJob._unmap(response)

    @cast_models
    def get_queue_job(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        queue_job_id: str,
    ) -> QueueJob:
        """Gets a job in a queue

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param queue_name: The queue name.
        :type queue_name: str
        :param queue_job_id: The job identifier. This is automatically generated and assigned when the job is created.
        :type queue_job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: QueueJob
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(queue_name)
        Validator(str).validate(queue_job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}/jobs/{{queue_job_id}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_path("queue_job_id", queue_job_id)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return QueueJob._unmap(response)

    @cast_models
    def delete_queue_job(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        queue_job_id: str,
    ) -> None:
        """Cancels a job in a queue

        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        :param project_name: Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.
        :type project_name: str
        :param queue_name: The queue name.
        :type queue_name: str
        :param queue_job_id: The job identifier. This is automatically generated and assigned when the job is created.
        :type queue_job_id: str
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
        ).validate(queue_name)
        Validator(str).validate(queue_job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}/jobs/{{queue_job_id}}",
                [self.get_api_key()],
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_path("queue_job_id", queue_job_id)
            .add_error(404, ProblemDetails)
            .add_error(429, ProblemDetails)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)
