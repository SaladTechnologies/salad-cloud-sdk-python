from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.webhook_secret_key import WebhookSecretKey
from ..models.utils.cast_models import cast_models


class WebhookSecretKeyService(BaseService):

    @cast_models
    def get_webhook_secret_key(self, organization_name: str) -> WebhookSecretKey:
        """Gets the webhook secret key

        :param organization_name: The unique organization name
        :type organization_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: WebhookSecretKey
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/webhook-secret-key",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return WebhookSecretKey._unmap(response)

    @cast_models
    def update_webhook_secret_key(self, organization_name: str) -> WebhookSecretKey:
        """Updates the webhook secret key

        :param organization_name: The unique organization name
        :type organization_name: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: WebhookSecretKey
        """

        Validator(str).min_length(2).max_length(63).pattern(
            "^[a-z][a-z0-9-]{0,61}[a-z0-9]$"
        ).validate(organization_name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/organizations/{{organization_name}}/webhook-secret-key",
                self.get_default_headers(),
            )
            .add_path("organization_name", organization_name)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return WebhookSecretKey._unmap(response)
