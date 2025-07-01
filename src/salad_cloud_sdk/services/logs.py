from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import LogEntryCollection, LogEntryQuery, ProblemDetails


class LogsService(BaseService):

    @cast_models
    def query_log_entries(
        self, request_body: LogEntryQuery, organization_name: str
    ) -> LogEntryCollection:
        """Retrieve a collection of _log entries_ for the _organization_ identified by `{organization_name}` matching the log query.

        :param request_body: The request body.
        :type request_body: LogEntryQuery
        :param organization_name: Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization.
        :type organization_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: LogEntryCollection
        """

        Validator(LogEntryQuery).validate(request_body)
        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/organizations/{{organization_name}}/log-entries",
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
        return LogEntryCollection._unmap(response)
