from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_queue import UpdateQueue
from ..models.queue_list import QueueList
from ..models.queue_job_list import QueueJobList
from ..models.queue_job import QueueJob
from ..models.queue import Queue
from ..models.create_queue_job import CreateQueueJob
from ..models.create_queue import CreateQueue


class QueuesService(BaseService):

    @cast_models
    def list_queues(self, organization_name: str, project_name: str) -> QueueList:
        """Gets the list of queues

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: QueueList
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return QueueList._unmap(response)

    @cast_models
    def create_queue(
        self, request_body: CreateQueue, organization_name: str, project_name: str
    ) -> Queue:
        """Creates a new queue

        :param request_body: The request body.
        :type request_body: CreateQueue
        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: Queue
        """

        Validator(CreateQueue).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(project_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return Queue._unmap(response)

    @cast_models
    def get_queue(
        self, organization_name: str, project_name: str, queue_name: str
    ) -> Queue:
        """Gets a queue

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param queue_name: The unique queue name
        :type queue_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Queue._unmap(response)

    @cast_models
    def update_queue(
        self,
        request_body: UpdateQueue,
        organization_name: str,
        project_name: str,
        queue_name: str,
    ) -> Queue:
        """Updates a queue

        :param request_body: The request body.
        :type request_body: UpdateQueue
        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param queue_name: The unique queue name
        :type queue_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: Queue
        """

        Validator(UpdateQueue).validate(request_body)
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body, "application/merge-patch+json")
        )

        response = self.send_request(serialized_request)
        return Queue._unmap(response)

    @cast_models
    def delete_queue(
        self, organization_name: str, project_name: str, queue_name: str
    ) -> Any:
        """Deletes a queue

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param queue_name: The unique queue name
        :type queue_name: str
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
        ).validate(queue_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def list_queue_jobs(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        page: int = None,
        page_size: int = None,
    ) -> QueueJobList:
        """Retrieves a list of queue jobs

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param queue_name: The unique queue name
        :type queue_name: str
        :param page: The page number, defaults to None
        :type page: int, optional
        :param page_size: The number of items per page, defaults to None
        :type page_size: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: QueueJobList
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}/jobs",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_query("page", page, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return QueueJobList._unmap(response)

    @cast_models
    def create_queue_job(
        self,
        request_body: CreateQueueJob,
        organization_name: str,
        project_name: str,
        queue_name: str,
    ) -> QueueJob:
        """Creates a new job

        :param request_body: The request body.
        :type request_body: CreateQueueJob
        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param queue_name: The unique queue name
        :type queue_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: QueueJob
        """

        Validator(CreateQueueJob).validate(request_body)
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}/jobs",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return QueueJob._unmap(response)

    @cast_models
    def get_queue_job(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        queue_job_id: str,
    ) -> QueueJob:
        """Retrieves a job in a queue

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param queue_name: The unique queue name
        :type queue_name: str
        :param queue_job_id: The unique job id
        :type queue_job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
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
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}/jobs/{{queue_job_id}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_path("queue_job_id", queue_job_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return QueueJob._unmap(response)

    @cast_models
    def delete_queue_job(
        self,
        organization_name: str,
        project_name: str,
        queue_name: str,
        queue_job_id: str,
    ) -> Any:
        """Deletes a queue job

        :param organization_name: The unique organization name
        :type organization_name: str
        :param project_name: The unique project name
        :type project_name: str
        :param queue_name: The unique queue name
        :type queue_name: str
        :param queue_job_id: The unique job id
        :type queue_job_id: str
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
        ).validate(queue_name)
        Validator(str).validate(queue_job_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/projects/{{project_name}}/queues/{{queue_name}}/jobs/{{queue_job_id}}",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .add_path("project_name", project_name)
            .add_path("queue_name", queue_name)
            .add_path("queue_job_id", queue_job_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return response
