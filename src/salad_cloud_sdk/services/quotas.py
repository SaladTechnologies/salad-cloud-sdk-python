from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.quotas import Quotas


class QuotasService(BaseService):

    @cast_models
    def get_quotas(self, organization_name: str) -> Quotas:
        """Gets the organization quotas

        :param organization_name: The unique organization name
        :type organization_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: Quotas
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/quotas",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Quotas._unmap(response)
