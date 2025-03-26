from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class WebhookSecretKey(BaseModel):
    """Represents a webhook secret key

    :param secret_key: The webhook secret key
    :type secret_key: str
    """

    def __init__(self, secret_key: str, **kwargs):
        """Represents a webhook secret key

        :param secret_key: The webhook secret key
        :type secret_key: str
        """
        self.secret_key = self._define_str(
            "secret_key",
            secret_key,
            pattern="^[+/=0-9A-Za-z]{44,172}$",
            min_length=44,
            max_length=172,
        )
        self._kwargs = kwargs
