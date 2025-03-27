from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ContainerRegistryAuthenticationAwsEcr(BaseModel):
    """Authentication details for AWS Elastic Container Registry (ECR)

    :param access_key_id: AWS access key ID used for ECR authentication
    :type access_key_id: str
    :param secret_access_key: AWS secret access key used for ECR authentication
    :type secret_access_key: str
    """

    def __init__(self, access_key_id: str, secret_access_key: str, **kwargs):
        """Authentication details for AWS Elastic Container Registry (ECR)

        :param access_key_id: AWS access key ID used for ECR authentication
        :type access_key_id: str
        :param secret_access_key: AWS secret access key used for ECR authentication
        :type secret_access_key: str
        """
        self.access_key_id = self._define_str(
            "access_key_id",
            access_key_id,
            pattern="^.*$",
            min_length=1,
            max_length=10000,
        )
        self.secret_access_key = self._define_str(
            "secret_access_key",
            secret_access_key,
            pattern="^.*$",
            min_length=1,
            max_length=10000,
        )
        self._kwargs = kwargs
