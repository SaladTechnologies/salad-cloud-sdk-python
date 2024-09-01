from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        cpu: int = None,
        memory: int = None,
        gpu_classes: List[str] = None,
        storage_amount: int = None,
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
        self.cpu = self._define_number("cpu", cpu, nullable=True, ge=1, le=16)
        self.memory = self._define_number(
            "memory", memory, nullable=True, ge=1024, le=30720
        )
        self.gpu_classes = gpu_classes
        self.storage_amount = self._define_number(
            "storage_amount",
            storage_amount,
            nullable=True,
            ge=1073741824,
            le=53687091200,
        )


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

    def __init__(self, host: str, api_token: str, dataset: str):
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


@JsonMap({})
class DatadogTags3(BaseModel):
    """DatadogTags3

    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str):
        """DatadogTags3

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value


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

    def __init__(self, host: str, api_key: str, tags: List[DatadogTags3] = None):
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
        self.tags = self._define_list(tags, DatadogTags3)


@JsonMap({})
class LoggingNewRelic3(BaseModel):
    """LoggingNewRelic3

    :param host: host
    :type host: str
    :param ingestion_key: ingestion_key
    :type ingestion_key: str
    """

    def __init__(self, host: str, ingestion_key: str):
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


@JsonMap({})
class LoggingSplunk3(BaseModel):
    """LoggingSplunk3

    :param host: host
    :type host: str
    :param token: token
    :type token: str
    """

    def __init__(self, host: str, token: str):
        """LoggingSplunk3

        :param host: host
        :type host: str
        :param token: token
        :type token: str
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.token = self._define_str("token", token, min_length=1, max_length=1000)


@JsonMap({})
class LoggingTcp3(BaseModel):
    """LoggingTcp3

    :param host: host
    :type host: str
    :param port: port
    :type port: int
    """

    def __init__(self, host: str, port: int):
        """LoggingTcp3

        :param host: host
        :type host: str
        :param port: port
        :type port: int
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.port = self._define_number("port", port, ge=1, le=65535)


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

    def __init__(self, name: str, value: str):
        """HttpHeaders4

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value


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
        user: str = None,
        password: str = None,
        path: str = None,
        headers: List[HttpHeaders4] = None,
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
        self.user = self._define_str("user", user, nullable=True)
        self.password = self._define_str("password", password, nullable=True)
        self.path = self._define_str("path", path, nullable=True)
        self.format = self._enum_matching(format, HttpFormat3.list(), "format")
        self.headers = self._define_list(headers, HttpHeaders4)
        self.compression = self._enum_matching(
            compression, HttpCompression3.list(), "compression"
        )


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
        axiom: LoggingAxiom3 = None,
        datadog: LoggingDatadog3 = None,
        new_relic: LoggingNewRelic3 = None,
        splunk: LoggingSplunk3 = None,
        tcp: LoggingTcp3 = None,
        http: LoggingHttp3 = None,
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
        self.axiom = self._define_object(axiom, LoggingAxiom3)
        self.datadog = self._define_object(datadog, LoggingDatadog3)
        self.new_relic = self._define_object(new_relic, LoggingNewRelic3)
        self.splunk = self._define_object(splunk, LoggingSplunk3)
        self.tcp = self._define_object(tcp, LoggingTcp3)
        self.http = self._define_object(http, LoggingHttp3)


@JsonMap({})
class RegistryAuthenticationBasic2(BaseModel):
    """RegistryAuthenticationBasic2

    :param username: username
    :type username: str
    :param password: password
    :type password: str
    """

    def __init__(self, username: str, password: str):
        """RegistryAuthenticationBasic2

        :param username: username
        :type username: str
        :param password: password
        :type password: str
        """
        self.username = username
        self.password = password


@JsonMap({})
class RegistryAuthenticationGcpGcr2(BaseModel):
    """RegistryAuthenticationGcpGcr2

    :param service_key: service_key
    :type service_key: str
    """

    def __init__(self, service_key: str):
        """RegistryAuthenticationGcpGcr2

        :param service_key: service_key
        :type service_key: str
        """
        self.service_key = service_key


@JsonMap({})
class RegistryAuthenticationAwsEcr2(BaseModel):
    """RegistryAuthenticationAwsEcr2

    :param access_key_id: access_key_id
    :type access_key_id: str
    :param secret_access_key: secret_access_key
    :type secret_access_key: str
    """

    def __init__(self, access_key_id: str, secret_access_key: str):
        """RegistryAuthenticationAwsEcr2

        :param access_key_id: access_key_id
        :type access_key_id: str
        :param secret_access_key: secret_access_key
        :type secret_access_key: str
        """
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key


@JsonMap({})
class RegistryAuthenticationDockerHub2(BaseModel):
    """RegistryAuthenticationDockerHub2

    :param username: username
    :type username: str
    :param personal_access_token: personal_access_token
    :type personal_access_token: str
    """

    def __init__(self, username: str, personal_access_token: str):
        """RegistryAuthenticationDockerHub2

        :param username: username
        :type username: str
        :param personal_access_token: personal_access_token
        :type personal_access_token: str
        """
        self.username = username
        self.personal_access_token = personal_access_token


@JsonMap({})
class RegistryAuthenticationGcpGar2(BaseModel):
    """RegistryAuthenticationGcpGar2

    :param service_key: service_key
    :type service_key: str
    """

    def __init__(self, service_key: str):
        """RegistryAuthenticationGcpGar2

        :param service_key: service_key
        :type service_key: str
        """
        self.service_key = service_key


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
        basic: RegistryAuthenticationBasic2 = None,
        gcp_gcr: RegistryAuthenticationGcpGcr2 = None,
        aws_ecr: RegistryAuthenticationAwsEcr2 = None,
        docker_hub: RegistryAuthenticationDockerHub2 = None,
        gcp_gar: RegistryAuthenticationGcpGar2 = None,
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
        self.basic = self._define_object(basic, RegistryAuthenticationBasic2)
        self.gcp_gcr = self._define_object(gcp_gcr, RegistryAuthenticationGcpGcr2)
        self.aws_ecr = self._define_object(aws_ecr, RegistryAuthenticationAwsEcr2)
        self.docker_hub = self._define_object(
            docker_hub, RegistryAuthenticationDockerHub2
        )
        self.gcp_gar = self._define_object(gcp_gar, RegistryAuthenticationGcpGar2)


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
    """

    def __init__(
        self,
        image: str = None,
        resources: Resources = None,
        command: List[str] = None,
        priority: ContainerGroupPriority = None,
        environment_variables: dict = None,
        logging: UpdateContainerLogging = None,
        registry_authentication: UpdateContainerRegistryAuthentication = None,
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
        """
        self.image = self._define_str(
            "image", image, nullable=True, min_length=1, max_length=1024
        )
        self.resources = self._define_object(resources, Resources)
        self.command = command
        self.priority = (
            self._enum_matching(priority, ContainerGroupPriority.list(), "priority")
            if priority
            else None
        )
        self.environment_variables = environment_variables
        self.logging = self._define_object(logging, UpdateContainerLogging)
        self.registry_authentication = self._define_object(
            registry_authentication, UpdateContainerRegistryAuthentication
        )
