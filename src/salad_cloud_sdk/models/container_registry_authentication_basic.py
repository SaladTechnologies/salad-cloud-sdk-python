from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerRegistryAuthenticationBasic(BaseModel):
    """Basic username and password authentication for generic container registries

    :param password: Password for registry authentication
    :type password: str
    :param username: Username for registry authentication
    :type username: str
    """

    def __init__(self, password: str, username: str, **kwargs):
        """Basic username and password authentication for generic container registries

        :param password: Password for registry authentication
        :type password: str
        :param username: Username for registry authentication
        :type username: str
        """
        self.password = self._define_str(
            "password", password, pattern="^.*$", min_length=1, max_length=10000
        )
        self.username = self._define_str(
            "username", username, pattern="^.*$", min_length=1, max_length=10000
        )
        self._kwargs = kwargs
