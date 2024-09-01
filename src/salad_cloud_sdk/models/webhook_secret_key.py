from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class WebhookSecretKey(BaseModel):
    """Represents a webhook secret key

    :param secret_key: The webhook secret key
    :type secret_key: str
    """

    def __init__(self, secret_key: str):
        """Represents a webhook secret key

        :param secret_key: The webhook secret key
        :type secret_key: str
        """
        self.secret_key = secret_key
