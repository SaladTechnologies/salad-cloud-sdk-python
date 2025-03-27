from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerRegistryAuthenticationDockerHub(BaseModel):
    """Authentication details for Docker Hub registry

    :param username: Docker Hub username
    :type username: str
    :param personal_access_token: Docker Hub personal access token (PAT)
    :type personal_access_token: str
    """

    def __init__(self, username: str, personal_access_token: str, **kwargs):
        """Authentication details for Docker Hub registry

        :param username: Docker Hub username
        :type username: str
        :param personal_access_token: Docker Hub personal access token (PAT)
        :type personal_access_token: str
        """
        self.username = self._define_str(
            "username", username, pattern="^.*$", min_length=1, max_length=10000
        )
        self.personal_access_token = self._define_str(
            "personal_access_token",
            personal_access_token,
            pattern="^.*$",
            min_length=1,
            max_length=10000,
        )
        self._kwargs = kwargs
