from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerRegistryAuthenticationDockerHub(BaseModel):
    """Authentication details for Docker Hub registry

    :param personal_access_token: Docker Hub personal access token (PAT)
    :type personal_access_token: str
    :param username: Docker Hub username
    :type username: str
    """

    def __init__(self, personal_access_token: str, username: str, **kwargs):
        """Authentication details for Docker Hub registry

        :param personal_access_token: Docker Hub personal access token (PAT)
        :type personal_access_token: str
        :param username: Docker Hub username
        :type username: str
        """
        self.personal_access_token = self._define_str(
            "personal_access_token",
            personal_access_token,
            pattern="^.*$",
            min_length=1,
            max_length=10000,
        )
        self.username = self._define_str(
            "username", username, pattern="^.*$", min_length=1, max_length=10000
        )
        self._kwargs = kwargs
