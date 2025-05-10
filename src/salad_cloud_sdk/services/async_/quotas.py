from typing import Awaitable, Union
from .utils.to_async import to_async
from ..quotas import QuotasService
from ...models import Quotas


class QuotasServiceAsync(QuotasService):
    """
    Async Wrapper for QuotasServiceAsync
    """

    def get_quotas(self, organization_name: str) -> Awaitable[Quotas]:
        return to_async(super().get_quotas)(organization_name)
