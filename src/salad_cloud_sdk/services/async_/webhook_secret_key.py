from typing import Awaitable, Union
from .utils.to_async import to_async
from ..webhook_secret_key import WebhookSecretKeyService
from ...models import WebhookSecretKey


class WebhookSecretKeyServiceAsync(WebhookSecretKeyService):
    """
    Async Wrapper for WebhookSecretKeyServiceAsync
    """

    def get_webhook_secret_key(
        self, organization_name: str
    ) -> Awaitable[WebhookSecretKey]:
        return to_async(super().get_webhook_secret_key)(organization_name)

    def update_webhook_secret_key(
        self, organization_name: str
    ) -> Awaitable[WebhookSecretKey]:
        return to_async(super().update_webhook_secret_key)(organization_name)
