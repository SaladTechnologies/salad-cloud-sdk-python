from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_resource_requirements import ContainerResourceRequirements
from .container_group_priority import ContainerGroupPriority


@JsonMap({})
class LoggingAxiom2(BaseModel):
    """LoggingAxiom2

    :param host: host
    :type host: str
    :param api_token: api_token
    :type api_token: str
    :param dataset: dataset
    :type dataset: str
    """

    def __init__(self, host: str, api_token: str, dataset: str):
        """LoggingAxiom2

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
class DatadogTags2(BaseModel):
    """DatadogTags2

    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str):
        """DatadogTags2

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value


@JsonMap({})
class LoggingDatadog2(BaseModel):
    """LoggingDatadog2

    :param host: host
    :type host: str
    :param api_key: api_key
    :type api_key: str
    :param tags: tags, defaults to None
    :type tags: List[DatadogTags2], optional
    """

    def __init__(self, host: str, api_key: str, tags: List[DatadogTags2] = None):
        """LoggingDatadog2

        :param host: host
        :type host: str
        :param api_key: api_key
        :type api_key: str
        :param tags: tags, defaults to None
        :type tags: List[DatadogTags2], optional
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.api_key = self._define_str(
            "api_key", api_key, min_length=1, max_length=1000
        )
        if tags is not None:
            self.tags = self._define_list(tags, DatadogTags2)


@JsonMap({})
class LoggingNewRelic2(BaseModel):
    """LoggingNewRelic2

    :param host: host
    :type host: str
    :param ingestion_key: ingestion_key
    :type ingestion_key: str
    """

    def __init__(self, host: str, ingestion_key: str):
        """LoggingNewRelic2

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
class LoggingSplunk2(BaseModel):
    """LoggingSplunk2

    :param host: host
    :type host: str
    :param token: token
    :type token: str
    """

    def __init__(self, host: str, token: str):
        """LoggingSplunk2

        :param host: host
        :type host: str
        :param token: token
        :type token: str
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.token = self._define_str("token", token, min_length=1, max_length=1000)


@JsonMap({})
class LoggingTcp2(BaseModel):
    """LoggingTcp2

    :param host: host
    :type host: str
    :param port: port
    :type port: int
    """

    def __init__(self, host: str, port: int):
        """LoggingTcp2

        :param host: host
        :type host: str
        :param port: port
        :type port: int
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.port = self._define_number("port", port, ge=1, le=65535)


class HttpFormat2(Enum):
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
        return list(map(lambda x: x.value, HttpFormat2._member_map_.values()))


@JsonMap({})
class HttpHeaders3(BaseModel):
    """HttpHeaders3

    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str):
        """HttpHeaders3

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value


class HttpCompression2(Enum):
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
        return list(map(lambda x: x.value, HttpCompression2._member_map_.values()))


@JsonMap({})
class LoggingHttp2(BaseModel):
    """LoggingHttp2

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
    :type format: HttpFormat2
    :param headers: headers, defaults to None
    :type headers: List[HttpHeaders3], optional
    :param compression: compression
    :type compression: HttpCompression2
    """

    def __init__(
        self,
        host: str,
        port: int,
        format: HttpFormat2,
        compression: HttpCompression2,
        user: str = None,
        password: str = None,
        path: str = None,
        headers: List[HttpHeaders3] = None,
    ):
        """LoggingHttp2

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
        :type format: HttpFormat2
        :param headers: headers, defaults to None
        :type headers: List[HttpHeaders3], optional
        :param compression: compression
        :type compression: HttpCompression2
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.port = self._define_number("port", port, ge=1, le=65535)
        if user is not None:
            self.user = self._define_str("user", user, nullable=True)
        if password is not None:
            self.password = self._define_str("password", password, nullable=True)
        if path is not None:
            self.path = self._define_str("path", path, nullable=True)
        self.format = self._enum_matching(format, HttpFormat2.list(), "format")
        if headers is not None:
            self.headers = self._define_list(headers, HttpHeaders3)
        self.compression = self._enum_matching(
            compression, HttpCompression2.list(), "compression"
        )


@JsonMap({})
class CreateContainerLogging(BaseModel):
    """CreateContainerLogging

    :param axiom: axiom, defaults to None
    :type axiom: LoggingAxiom2, optional
    :param datadog: datadog, defaults to None
    :type datadog: LoggingDatadog2, optional
    :param new_relic: new_relic, defaults to None
    :type new_relic: LoggingNewRelic2, optional
    :param splunk: splunk, defaults to None
    :type splunk: LoggingSplunk2, optional
    :param tcp: tcp, defaults to None
    :type tcp: LoggingTcp2, optional
    :param http: http, defaults to None
    :type http: LoggingHttp2, optional
    """

    def __init__(
        self,
        axiom: LoggingAxiom2 = None,
        datadog: LoggingDatadog2 = None,
        new_relic: LoggingNewRelic2 = None,
        splunk: LoggingSplunk2 = None,
        tcp: LoggingTcp2 = None,
        http: LoggingHttp2 = None,
    ):
        """CreateContainerLogging

        :param axiom: axiom, defaults to None
        :type axiom: LoggingAxiom2, optional
        :param datadog: datadog, defaults to None
        :type datadog: LoggingDatadog2, optional
        :param new_relic: new_relic, defaults to None
        :type new_relic: LoggingNewRelic2, optional
        :param splunk: splunk, defaults to None
        :type splunk: LoggingSplunk2, optional
        :param tcp: tcp, defaults to None
        :type tcp: LoggingTcp2, optional
        :param http: http, defaults to None
        :type http: LoggingHttp2, optional
        """
        if axiom is not None:
            self.axiom = self._define_object(axiom, LoggingAxiom2)
        if datadog is not None:
            self.datadog = self._define_object(datadog, LoggingDatadog2)
        if new_relic is not None:
            self.new_relic = self._define_object(new_relic, LoggingNewRelic2)
        if splunk is not None:
            self.splunk = self._define_object(splunk, LoggingSplunk2)
        if tcp is not None:
            self.tcp = self._define_object(tcp, LoggingTcp2)
        if http is not None:
            self.http = self._define_object(http, LoggingHttp2)


@JsonMap({})
class RegistryAuthenticationBasic1(BaseModel):
    """RegistryAuthenticationBasic1

    :param username: username
    :type username: str
    :param password: password
    :type password: str
    """

    def __init__(self, username: str, password: str):
        """RegistryAuthenticationBasic1

        :param username: username
        :type username: str
        :param password: password
        :type password: str
        """
        self.username = username
        self.password = password


@JsonMap({})
class RegistryAuthenticationGcpGcr1(BaseModel):
    """RegistryAuthenticationGcpGcr1

    :param service_key: service_key
    :type service_key: str
    """

    def __init__(self, service_key: str):
        """RegistryAuthenticationGcpGcr1

        :param service_key: service_key
        :type service_key: str
        """
        self.service_key = service_key


@JsonMap({})
class RegistryAuthenticationAwsEcr1(BaseModel):
    """RegistryAuthenticationAwsEcr1

    :param access_key_id: access_key_id
    :type access_key_id: str
    :param secret_access_key: secret_access_key
    :type secret_access_key: str
    """

    def __init__(self, access_key_id: str, secret_access_key: str):
        """RegistryAuthenticationAwsEcr1

        :param access_key_id: access_key_id
        :type access_key_id: str
        :param secret_access_key: secret_access_key
        :type secret_access_key: str
        """
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key


@JsonMap({})
class RegistryAuthenticationDockerHub1(BaseModel):
    """RegistryAuthenticationDockerHub1

    :param username: username
    :type username: str
    :param personal_access_token: personal_access_token
    :type personal_access_token: str
    """

    def __init__(self, username: str, personal_access_token: str):
        """RegistryAuthenticationDockerHub1

        :param username: username
        :type username: str
        :param personal_access_token: personal_access_token
        :type personal_access_token: str
        """
        self.username = username
        self.personal_access_token = personal_access_token


@JsonMap({})
class RegistryAuthenticationGcpGar1(BaseModel):
    """RegistryAuthenticationGcpGar1

    :param service_key: service_key
    :type service_key: str
    """

    def __init__(self, service_key: str):
        """RegistryAuthenticationGcpGar1

        :param service_key: service_key
        :type service_key: str
        """
        self.service_key = service_key


@JsonMap({})
class CreateContainerRegistryAuthentication(BaseModel):
    """CreateContainerRegistryAuthentication

    :param basic: basic, defaults to None
    :type basic: RegistryAuthenticationBasic1, optional
    :param gcp_gcr: gcp_gcr, defaults to None
    :type gcp_gcr: RegistryAuthenticationGcpGcr1, optional
    :param aws_ecr: aws_ecr, defaults to None
    :type aws_ecr: RegistryAuthenticationAwsEcr1, optional
    :param docker_hub: docker_hub, defaults to None
    :type docker_hub: RegistryAuthenticationDockerHub1, optional
    :param gcp_gar: gcp_gar, defaults to None
    :type gcp_gar: RegistryAuthenticationGcpGar1, optional
    """

    def __init__(
        self,
        basic: RegistryAuthenticationBasic1 = None,
        gcp_gcr: RegistryAuthenticationGcpGcr1 = None,
        aws_ecr: RegistryAuthenticationAwsEcr1 = None,
        docker_hub: RegistryAuthenticationDockerHub1 = None,
        gcp_gar: RegistryAuthenticationGcpGar1 = None,
    ):
        """CreateContainerRegistryAuthentication

        :param basic: basic, defaults to None
        :type basic: RegistryAuthenticationBasic1, optional
        :param gcp_gcr: gcp_gcr, defaults to None
        :type gcp_gcr: RegistryAuthenticationGcpGcr1, optional
        :param aws_ecr: aws_ecr, defaults to None
        :type aws_ecr: RegistryAuthenticationAwsEcr1, optional
        :param docker_hub: docker_hub, defaults to None
        :type docker_hub: RegistryAuthenticationDockerHub1, optional
        :param gcp_gar: gcp_gar, defaults to None
        :type gcp_gar: RegistryAuthenticationGcpGar1, optional
        """
        if basic is not None:
            self.basic = self._define_object(basic, RegistryAuthenticationBasic1)
        if gcp_gcr is not None:
            self.gcp_gcr = self._define_object(gcp_gcr, RegistryAuthenticationGcpGcr1)
        if aws_ecr is not None:
            self.aws_ecr = self._define_object(aws_ecr, RegistryAuthenticationAwsEcr1)
        if docker_hub is not None:
            self.docker_hub = self._define_object(
                docker_hub, RegistryAuthenticationDockerHub1
            )
        if gcp_gar is not None:
            self.gcp_gar = self._define_object(gcp_gar, RegistryAuthenticationGcpGar1)


@JsonMap({})
class CreateContainer(BaseModel):
    """Represents a container

    :param image: image
    :type image: str
    :param resources: Represents a container resource requirements
    :type resources: ContainerResourceRequirements
    :param command: Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image., defaults to None
    :type command: List[str], optional
    :param priority: priority, defaults to None
    :type priority: ContainerGroupPriority, optional
    :param environment_variables: environment_variables, defaults to None
    :type environment_variables: dict, optional
    :param logging: logging, defaults to None
    :type logging: CreateContainerLogging, optional
    :param registry_authentication: registry_authentication, defaults to None
    :type registry_authentication: CreateContainerRegistryAuthentication, optional
    """

    def __init__(
        self,
        image: str,
        resources: ContainerResourceRequirements,
        command: List[str] = None,
        priority: ContainerGroupPriority = None,
        environment_variables: dict = None,
        logging: CreateContainerLogging = None,
        registry_authentication: CreateContainerRegistryAuthentication = None,
    ):
        """Represents a container

        :param image: image
        :type image: str
        :param resources: Represents a container resource requirements
        :type resources: ContainerResourceRequirements
        :param command: Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image., defaults to None
        :type command: List[str], optional
        :param priority: priority, defaults to None
        :type priority: ContainerGroupPriority, optional
        :param environment_variables: environment_variables, defaults to None
        :type environment_variables: dict, optional
        :param logging: logging, defaults to None
        :type logging: CreateContainerLogging, optional
        :param registry_authentication: registry_authentication, defaults to None
        :type registry_authentication: CreateContainerRegistryAuthentication, optional
        """
        self.image = self._define_str("image", image, min_length=1, max_length=1024)
        self.resources = self._define_object(resources, ContainerResourceRequirements)
        if command is not None:
            self.command = command
        if priority is not None:
            self.priority = self._enum_matching(
                priority, ContainerGroupPriority.list(), "priority"
            )
        if environment_variables is not None:
            self.environment_variables = environment_variables
        if logging is not None:
            self.logging = self._define_object(logging, CreateContainerLogging)
        if registry_authentication is not None:
            self.registry_authentication = self._define_object(
                registry_authentication, CreateContainerRegistryAuthentication
            )
