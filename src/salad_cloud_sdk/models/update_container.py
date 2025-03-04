from __future__ import annotations
from enum import Enum
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_group_priority import ContainerGroupPriority


@JsonMap({})
class Resources(BaseModel):
    """Resources

    :param cpu: cpu, defaults to None
    :type cpu: int, optional
    :param memory: memory, defaults to None
    :type memory: int, optional
    :param gpu_classes: gpu_classes, defaults to None
    :type gpu_classes: List[str], optional
    :param storage_amount: storage_amount, defaults to None
    :type storage_amount: int, optional
    """

    def __init__(
        self,
        cpu: Union[int, None] = SENTINEL,
        memory: Union[int, None] = SENTINEL,
        gpu_classes: Union[List[str], None] = SENTINEL,
        storage_amount: Union[int, None] = SENTINEL,
        **kwargs,
    ):
        """Resources

        :param cpu: cpu, defaults to None
        :type cpu: int, optional
        :param memory: memory, defaults to None
        :type memory: int, optional
        :param gpu_classes: gpu_classes, defaults to None
        :type gpu_classes: List[str], optional
        :param storage_amount: storage_amount, defaults to None
        :type storage_amount: int, optional
        """
        if cpu is not SENTINEL:
            self.cpu = self._define_number("cpu", cpu, nullable=True, ge=1, le=16)
        if memory is not SENTINEL:
            self.memory = self._define_number(
                "memory", memory, nullable=True, ge=1024, le=61440
            )
        if gpu_classes is not SENTINEL:
            self.gpu_classes = gpu_classes
        if storage_amount is not SENTINEL:
            self.storage_amount = self._define_number(
                "storage_amount",
                storage_amount,
                nullable=True,
                ge=1073741824,
                le=53687091200,
            )
        self._kwargs = kwargs


@JsonMap({})
class LoggingAxiom3(BaseModel):
    """LoggingAxiom3

    :param host: host
    :type host: str
    :param api_token: api_token
    :type api_token: str
    :param dataset: dataset
    :type dataset: str
    """

    def __init__(self, host: str, api_token: str, dataset: str, **kwargs):
        """LoggingAxiom3

        :param host: host
        :type host: str
        :param api_token: api_token
        :type api_token: str
        :param dataset: dataset
        :type dataset: str
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.api_token = self._define_str(
            "api_token", api_token, min_length=1, max_length=1000
        )
        self.dataset = self._define_str(
            "dataset", dataset, min_length=1, max_length=1000
        )
        self._kwargs = kwargs


@JsonMap({})
class DatadogTags3(BaseModel):
    """DatadogTags3

    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str, **kwargs):
        """DatadogTags3

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value
        self._kwargs = kwargs


@JsonMap({})
class LoggingDatadog3(BaseModel):
    """LoggingDatadog3

    :param host: host
    :type host: str
    :param api_key: api_key
    :type api_key: str
    :param tags: tags, defaults to None
    :type tags: List[DatadogTags3], optional
    """

    def __init__(
        self,
        host: str,
        api_key: str,
        tags: Union[List[DatadogTags3], None] = SENTINEL,
        **kwargs,
    ):
        """LoggingDatadog3

        :param host: host
        :type host: str
        :param api_key: api_key
        :type api_key: str
        :param tags: tags, defaults to None
        :type tags: List[DatadogTags3], optional
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.api_key = self._define_str(
            "api_key", api_key, min_length=1, max_length=1000
        )
        if tags is not SENTINEL:
            self.tags = self._define_list(tags, DatadogTags3)
        self._kwargs = kwargs


@JsonMap({})
class LoggingNewRelic3(BaseModel):
    """LoggingNewRelic3

    :param host: host
    :type host: str
    :param ingestion_key: ingestion_key
    :type ingestion_key: str
    """

    def __init__(self, host: str, ingestion_key: str, **kwargs):
        """LoggingNewRelic3

        :param host: host
        :type host: str
        :param ingestion_key: ingestion_key
        :type ingestion_key: str
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.ingestion_key = self._define_str(
            "ingestion_key", ingestion_key, min_length=1, max_length=1000
        )
        self._kwargs = kwargs


@JsonMap({})
class LoggingSplunk3(BaseModel):
    """LoggingSplunk3

    :param host: host
    :type host: str
    :param token: token
    :type token: str
    """

    def __init__(self, host: str, token: str, **kwargs):
        """LoggingSplunk3

        :param host: host
        :type host: str
        :param token: token
        :type token: str
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.token = self._define_str("token", token, min_length=1, max_length=1000)
        self._kwargs = kwargs


@JsonMap({})
class LoggingTcp3(BaseModel):
    """LoggingTcp3

    :param host: host
    :type host: str
    :param port: port
    :type port: int
    """

    def __init__(self, host: str, port: int, **kwargs):
        """LoggingTcp3

        :param host: host
        :type host: str
        :param port: port
        :type port: int
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.port = self._define_number("port", port, ge=1, le=65535)
        self._kwargs = kwargs


class HttpFormat3(Enum):
    """An enumeration representing different categories.

    :cvar JSON: "json"
    :vartype JSON: str
    :cvar JSONLINES: "json_lines"
    :vartype JSONLINES: str
    """

    JSON = "json"
    JSONLINES = "json_lines"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, HttpFormat3._member_map_.values()))


@JsonMap({})
class HttpHeaders4(BaseModel):
    """HttpHeaders4

    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str, **kwargs):
        """HttpHeaders4

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value
        self._kwargs = kwargs


class HttpCompression3(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "none"
    :vartype NONE: str
    :cvar GZIP: "gzip"
    :vartype GZIP: str
    """

    NONE = "none"
    GZIP = "gzip"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, HttpCompression3._member_map_.values()))


@JsonMap({})
class LoggingHttp3(BaseModel):
    """LoggingHttp3

    :param host: host
    :type host: str
    :param port: port
    :type port: int
    :param user: user, defaults to None
    :type user: str, optional
    :param password: password, defaults to None
    :type password: str, optional
    :param path: path, defaults to None
    :type path: str, optional
    :param format: format
    :type format: HttpFormat3
    :param headers: headers, defaults to None
    :type headers: List[HttpHeaders4], optional
    :param compression: compression
    :type compression: HttpCompression3
    """

    def __init__(
        self,
        host: str,
        port: int,
        format: HttpFormat3,
        compression: HttpCompression3,
        user: Union[str, None] = SENTINEL,
        password: Union[str, None] = SENTINEL,
        path: Union[str, None] = SENTINEL,
        headers: Union[List[HttpHeaders4], None] = SENTINEL,
        **kwargs,
    ):
        """LoggingHttp3

        :param host: host
        :type host: str
        :param port: port
        :type port: int
        :param user: user, defaults to None
        :type user: str, optional
        :param password: password, defaults to None
        :type password: str, optional
        :param path: path, defaults to None
        :type path: str, optional
        :param format: format
        :type format: HttpFormat3
        :param headers: headers, defaults to None
        :type headers: List[HttpHeaders4], optional
        :param compression: compression
        :type compression: HttpCompression3
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.port = self._define_number("port", port, ge=1, le=65535)
        if user is not SENTINEL:
            self.user = self._define_str("user", user, nullable=True)
        if password is not SENTINEL:
            self.password = self._define_str("password", password, nullable=True)
        if path is not SENTINEL:
            self.path = self._define_str("path", path, nullable=True)
        self.format = self._enum_matching(format, HttpFormat3.list(), "format")
        if headers is not SENTINEL:
            self.headers = self._define_list(headers, HttpHeaders4)
        self.compression = self._enum_matching(
            compression, HttpCompression3.list(), "compression"
        )
        self._kwargs = kwargs


@JsonMap({})
class UpdateContainerLogging(BaseModel):
    """UpdateContainerLogging

    :param axiom: axiom, defaults to None
    :type axiom: LoggingAxiom3, optional
    :param datadog: datadog, defaults to None
    :type datadog: LoggingDatadog3, optional
    :param new_relic: new_relic, defaults to None
    :type new_relic: LoggingNewRelic3, optional
    :param splunk: splunk, defaults to None
    :type splunk: LoggingSplunk3, optional
    :param tcp: tcp, defaults to None
    :type tcp: LoggingTcp3, optional
    :param http: http, defaults to None
    :type http: LoggingHttp3, optional
    """

    def __init__(
        self,
        axiom: Union[LoggingAxiom3, None] = SENTINEL,
        datadog: Union[LoggingDatadog3, None] = SENTINEL,
        new_relic: Union[LoggingNewRelic3, None] = SENTINEL,
        splunk: Union[LoggingSplunk3, None] = SENTINEL,
        tcp: Union[LoggingTcp3, None] = SENTINEL,
        http: Union[LoggingHttp3, None] = SENTINEL,
        **kwargs,
    ):
        """UpdateContainerLogging

        :param axiom: axiom, defaults to None
        :type axiom: LoggingAxiom3, optional
        :param datadog: datadog, defaults to None
        :type datadog: LoggingDatadog3, optional
        :param new_relic: new_relic, defaults to None
        :type new_relic: LoggingNewRelic3, optional
        :param splunk: splunk, defaults to None
        :type splunk: LoggingSplunk3, optional
        :param tcp: tcp, defaults to None
        :type tcp: LoggingTcp3, optional
        :param http: http, defaults to None
        :type http: LoggingHttp3, optional
        """
        if axiom is not SENTINEL:
            self.axiom = self._define_object(axiom, LoggingAxiom3)
        if datadog is not SENTINEL:
            self.datadog = self._define_object(datadog, LoggingDatadog3)
        if new_relic is not SENTINEL:
            self.new_relic = self._define_object(new_relic, LoggingNewRelic3)
        if splunk is not SENTINEL:
            self.splunk = self._define_object(splunk, LoggingSplunk3)
        if tcp is not SENTINEL:
            self.tcp = self._define_object(tcp, LoggingTcp3)
        if http is not SENTINEL:
            self.http = self._define_object(http, LoggingHttp3)
        self._kwargs = kwargs


@JsonMap({})
class RegistryAuthenticationBasic2(BaseModel):
    """RegistryAuthenticationBasic2

    :param username: username
    :type username: str
    :param password: password
    :type password: str
    """

    def __init__(self, username: str, password: str, **kwargs):
        """RegistryAuthenticationBasic2

        :param username: username
        :type username: str
        :param password: password
        :type password: str
        """
        self.username = username
        self.password = password
        self._kwargs = kwargs


@JsonMap({})
class RegistryAuthenticationGcpGcr2(BaseModel):
    """RegistryAuthenticationGcpGcr2

    :param service_key: service_key
    :type service_key: str
    """

    def __init__(self, service_key: str, **kwargs):
        """RegistryAuthenticationGcpGcr2

        :param service_key: service_key
        :type service_key: str
        """
        self.service_key = service_key
        self._kwargs = kwargs


@JsonMap({})
class RegistryAuthenticationAwsEcr2(BaseModel):
    """RegistryAuthenticationAwsEcr2

    :param access_key_id: access_key_id
    :type access_key_id: str
    :param secret_access_key: secret_access_key
    :type secret_access_key: str
    """

    def __init__(self, access_key_id: str, secret_access_key: str, **kwargs):
        """RegistryAuthenticationAwsEcr2

        :param access_key_id: access_key_id
        :type access_key_id: str
        :param secret_access_key: secret_access_key
        :type secret_access_key: str
        """
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self._kwargs = kwargs


@JsonMap({})
class RegistryAuthenticationDockerHub2(BaseModel):
    """RegistryAuthenticationDockerHub2

    :param username: username
    :type username: str
    :param personal_access_token: personal_access_token
    :type personal_access_token: str
    """

    def __init__(self, username: str, personal_access_token: str, **kwargs):
        """RegistryAuthenticationDockerHub2

        :param username: username
        :type username: str
        :param personal_access_token: personal_access_token
        :type personal_access_token: str
        """
        self.username = username
        self.personal_access_token = personal_access_token
        self._kwargs = kwargs


@JsonMap({})
class RegistryAuthenticationGcpGar2(BaseModel):
    """RegistryAuthenticationGcpGar2

    :param service_key: service_key
    :type service_key: str
    """

    def __init__(self, service_key: str, **kwargs):
        """RegistryAuthenticationGcpGar2

        :param service_key: service_key
        :type service_key: str
        """
        self.service_key = service_key
        self._kwargs = kwargs


@JsonMap({})
class UpdateContainerRegistryAuthentication(BaseModel):
    """UpdateContainerRegistryAuthentication

    :param basic: basic, defaults to None
    :type basic: RegistryAuthenticationBasic2, optional
    :param gcp_gcr: gcp_gcr, defaults to None
    :type gcp_gcr: RegistryAuthenticationGcpGcr2, optional
    :param aws_ecr: aws_ecr, defaults to None
    :type aws_ecr: RegistryAuthenticationAwsEcr2, optional
    :param docker_hub: docker_hub, defaults to None
    :type docker_hub: RegistryAuthenticationDockerHub2, optional
    :param gcp_gar: gcp_gar, defaults to None
    :type gcp_gar: RegistryAuthenticationGcpGar2, optional
    """

    def __init__(
        self,
        basic: Union[RegistryAuthenticationBasic2, None] = SENTINEL,
        gcp_gcr: Union[RegistryAuthenticationGcpGcr2, None] = SENTINEL,
        aws_ecr: Union[RegistryAuthenticationAwsEcr2, None] = SENTINEL,
        docker_hub: Union[RegistryAuthenticationDockerHub2, None] = SENTINEL,
        gcp_gar: Union[RegistryAuthenticationGcpGar2, None] = SENTINEL,
        **kwargs,
    ):
        """UpdateContainerRegistryAuthentication

        :param basic: basic, defaults to None
        :type basic: RegistryAuthenticationBasic2, optional
        :param gcp_gcr: gcp_gcr, defaults to None
        :type gcp_gcr: RegistryAuthenticationGcpGcr2, optional
        :param aws_ecr: aws_ecr, defaults to None
        :type aws_ecr: RegistryAuthenticationAwsEcr2, optional
        :param docker_hub: docker_hub, defaults to None
        :type docker_hub: RegistryAuthenticationDockerHub2, optional
        :param gcp_gar: gcp_gar, defaults to None
        :type gcp_gar: RegistryAuthenticationGcpGar2, optional
        """
        if basic is not SENTINEL:
            self.basic = self._define_object(basic, RegistryAuthenticationBasic2)
        if gcp_gcr is not SENTINEL:
            self.gcp_gcr = self._define_object(gcp_gcr, RegistryAuthenticationGcpGcr2)
        if aws_ecr is not SENTINEL:
            self.aws_ecr = self._define_object(aws_ecr, RegistryAuthenticationAwsEcr2)
        if docker_hub is not SENTINEL:
            self.docker_hub = self._define_object(
                docker_hub, RegistryAuthenticationDockerHub2
            )
        if gcp_gar is not SENTINEL:
            self.gcp_gar = self._define_object(gcp_gar, RegistryAuthenticationGcpGar2)
        self._kwargs = kwargs


@JsonMap({})
class UpdateContainer(BaseModel):
    """Represents an update container object

    :param image: image, defaults to None
    :type image: str, optional
    :param resources: resources, defaults to None
    :type resources: Resources, optional
    :param command: Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image., defaults to None
    :type command: List[str], optional
    :param priority: priority, defaults to None
    :type priority: ContainerGroupPriority, optional
    :param environment_variables: environment_variables, defaults to None
    :type environment_variables: dict, optional
    :param logging: logging, defaults to None
    :type logging: UpdateContainerLogging, optional
    :param registry_authentication: registry_authentication, defaults to None
    :type registry_authentication: UpdateContainerRegistryAuthentication, optional
    :param image_caching: image_caching, defaults to None
    :type image_caching: bool, optional
    """

    def __init__(
        self,
        image: Union[str, None] = SENTINEL,
        resources: Union[Resources, None] = SENTINEL,
        command: Union[List[str], None] = SENTINEL,
        priority: Union[ContainerGroupPriority, None] = SENTINEL,
        environment_variables: dict = SENTINEL,
        logging: Union[UpdateContainerLogging, None] = SENTINEL,
        registry_authentication: Union[
            UpdateContainerRegistryAuthentication, None
        ] = SENTINEL,
        image_caching: bool = SENTINEL,
        **kwargs,
    ):
        """Represents an update container object

        :param image: image, defaults to None
        :type image: str, optional
        :param resources: resources, defaults to None
        :type resources: Resources, optional
        :param command: Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image., defaults to None
        :type command: List[str], optional
        :param priority: priority, defaults to None
        :type priority: ContainerGroupPriority, optional
        :param environment_variables: environment_variables, defaults to None
        :type environment_variables: dict, optional
        :param logging: logging, defaults to None
        :type logging: UpdateContainerLogging, optional
        :param registry_authentication: registry_authentication, defaults to None
        :type registry_authentication: UpdateContainerRegistryAuthentication, optional
        :param image_caching: image_caching, defaults to None
        :type image_caching: bool, optional
        """
        if image is not SENTINEL:
            self.image = self._define_str(
                "image", image, nullable=True, min_length=1, max_length=1024
            )
        if resources is not SENTINEL:
            self.resources = self._define_object(resources, Resources)
        if command is not SENTINEL:
            self.command = command
        if priority is not SENTINEL:
            self.priority = self._enum_matching(
                priority, ContainerGroupPriority.list(), "priority"
            )
        if environment_variables is not SENTINEL:
            self.environment_variables = environment_variables
        if logging is not SENTINEL:
            self.logging = self._define_object(logging, UpdateContainerLogging)
        if registry_authentication is not SENTINEL:
            self.registry_authentication = self._define_object(
                registry_authentication, UpdateContainerRegistryAuthentication
            )
        if image_caching is not SENTINEL:
            self.image_caching = image_caching
        self._kwargs = kwargs
