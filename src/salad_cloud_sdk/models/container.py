from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_resource_requirements import ContainerResourceRequirements
from .container_group_priority import ContainerGroupPriority


@JsonMap({})
class LoggingAxiom1(BaseModel):
    """LoggingAxiom1

    :param host: host
    :type host: str
    :param api_token: api_token
    :type api_token: str
    :param dataset: dataset
    :type dataset: str
    """

    def __init__(self, host: str, api_token: str, dataset: str):
        """LoggingAxiom1

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
class DatadogTags1(BaseModel):
    """DatadogTags1

    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str):
        """DatadogTags1

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value


@JsonMap({})
class LoggingDatadog1(BaseModel):
    """LoggingDatadog1

    :param host: host
    :type host: str
    :param api_key: api_key
    :type api_key: str
    :param tags: tags, defaults to None
    :type tags: List[DatadogTags1], optional
    """

    def __init__(self, host: str, api_key: str, tags: List[DatadogTags1] = None):
        """LoggingDatadog1

        :param host: host
        :type host: str
        :param api_key: api_key
        :type api_key: str
        :param tags: tags, defaults to None
        :type tags: List[DatadogTags1], optional
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.api_key = self._define_str(
            "api_key", api_key, min_length=1, max_length=1000
        )
        self.tags = self._define_list(tags, DatadogTags1)


@JsonMap({})
class LoggingNewRelic1(BaseModel):
    """LoggingNewRelic1

    :param host: host
    :type host: str
    :param ingestion_key: ingestion_key
    :type ingestion_key: str
    """

    def __init__(self, host: str, ingestion_key: str):
        """LoggingNewRelic1

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
class LoggingSplunk1(BaseModel):
    """LoggingSplunk1

    :param host: host
    :type host: str
    :param token: token
    :type token: str
    """

    def __init__(self, host: str, token: str):
        """LoggingSplunk1

        :param host: host
        :type host: str
        :param token: token
        :type token: str
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.token = self._define_str("token", token, min_length=1, max_length=1000)


@JsonMap({})
class LoggingTcp1(BaseModel):
    """LoggingTcp1

    :param host: host
    :type host: str
    :param port: port
    :type port: int
    """

    def __init__(self, host: str, port: int):
        """LoggingTcp1

        :param host: host
        :type host: str
        :param port: port
        :type port: int
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.port = self._define_number("port", port, ge=1, le=65535)


class HttpFormat1(Enum):
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
        return list(map(lambda x: x.value, HttpFormat1._member_map_.values()))


@JsonMap({})
class HttpHeaders1(BaseModel):
    """HttpHeaders1

    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str):
        """HttpHeaders1

        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        self.name = name
        self.value = value


class HttpCompression1(Enum):
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
        return list(map(lambda x: x.value, HttpCompression1._member_map_.values()))


@JsonMap({})
class LoggingHttp1(BaseModel):
    """LoggingHttp1

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
    :type format: HttpFormat1
    :param headers: headers, defaults to None
    :type headers: List[HttpHeaders1], optional
    :param compression: compression
    :type compression: HttpCompression1
    """

    def __init__(
        self,
        host: str,
        port: int,
        format: HttpFormat1,
        compression: HttpCompression1,
        user: str = None,
        password: str = None,
        path: str = None,
        headers: List[HttpHeaders1] = None,
    ):
        """LoggingHttp1

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
        :type format: HttpFormat1
        :param headers: headers, defaults to None
        :type headers: List[HttpHeaders1], optional
        :param compression: compression
        :type compression: HttpCompression1
        """
        self.host = self._define_str("host", host, min_length=1, max_length=1000)
        self.port = self._define_number("port", port, ge=1, le=65535)
        self.user = self._define_str("user", user, nullable=True)
        self.password = self._define_str("password", password, nullable=True)
        self.path = self._define_str("path", path, nullable=True)
        self.format = self._enum_matching(format, HttpFormat1.list(), "format")
        self.headers = self._define_list(headers, HttpHeaders1)
        self.compression = self._enum_matching(
            compression, HttpCompression1.list(), "compression"
        )


@JsonMap({})
class ContainerLogging(BaseModel):
    """ContainerLogging

    :param axiom: axiom, defaults to None
    :type axiom: LoggingAxiom1, optional
    :param datadog: datadog, defaults to None
    :type datadog: LoggingDatadog1, optional
    :param new_relic: new_relic, defaults to None
    :type new_relic: LoggingNewRelic1, optional
    :param splunk: splunk, defaults to None
    :type splunk: LoggingSplunk1, optional
    :param tcp: tcp, defaults to None
    :type tcp: LoggingTcp1, optional
    :param http: http, defaults to None
    :type http: LoggingHttp1, optional
    """

    def __init__(
        self,
        axiom: LoggingAxiom1 = None,
        datadog: LoggingDatadog1 = None,
        new_relic: LoggingNewRelic1 = None,
        splunk: LoggingSplunk1 = None,
        tcp: LoggingTcp1 = None,
        http: LoggingHttp1 = None,
    ):
        """ContainerLogging

        :param axiom: axiom, defaults to None
        :type axiom: LoggingAxiom1, optional
        :param datadog: datadog, defaults to None
        :type datadog: LoggingDatadog1, optional
        :param new_relic: new_relic, defaults to None
        :type new_relic: LoggingNewRelic1, optional
        :param splunk: splunk, defaults to None
        :type splunk: LoggingSplunk1, optional
        :param tcp: tcp, defaults to None
        :type tcp: LoggingTcp1, optional
        :param http: http, defaults to None
        :type http: LoggingHttp1, optional
        """
        self.axiom = self._define_object(axiom, LoggingAxiom1)
        self.datadog = self._define_object(datadog, LoggingDatadog1)
        self.new_relic = self._define_object(new_relic, LoggingNewRelic1)
        self.splunk = self._define_object(splunk, LoggingSplunk1)
        self.tcp = self._define_object(tcp, LoggingTcp1)
        self.http = self._define_object(http, LoggingHttp1)


@JsonMap({})
class Container(BaseModel):
    """Represents a container

    :param image: image
    :type image: str
    :param resources: Represents a container resource requirements
    :type resources: ContainerResourceRequirements
    :param command: command
    :type command: List[str]
    :param priority: priority, defaults to None
    :type priority: ContainerGroupPriority, optional
    :param size: size, defaults to None
    :type size: int, optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param environment_variables: environment_variables, defaults to None
    :type environment_variables: dict, optional
    :param logging: logging, defaults to None
    :type logging: ContainerLogging, optional
    """

    def __init__(
        self,
        image: str,
        resources: ContainerResourceRequirements,
        command: List[str],
        priority: ContainerGroupPriority = None,
        size: int = None,
        hash: str = None,
        environment_variables: dict = None,
        logging: ContainerLogging = None,
    ):
        """Represents a container

        :param image: image
        :type image: str
        :param resources: Represents a container resource requirements
        :type resources: ContainerResourceRequirements
        :param command: command
        :type command: List[str]
        :param priority: priority, defaults to None
        :type priority: ContainerGroupPriority, optional
        :param size: size, defaults to None
        :type size: int, optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param environment_variables: environment_variables, defaults to None
        :type environment_variables: dict, optional
        :param logging: logging, defaults to None
        :type logging: ContainerLogging, optional
        """
        self.image = self._define_str("image", image, min_length=1, max_length=1024)
        self.resources = self._define_object(resources, ContainerResourceRequirements)
        self.command = command
        self.priority = (
            self._enum_matching(priority, ContainerGroupPriority.list(), "priority")
            if priority
            else None
        )
        self.size = self._define_number("size", size, nullable=True)
        self.hash = self._define_str("hash", hash, nullable=True)
        self.environment_variables = environment_variables
        self.logging = self._define_object(logging, ContainerLogging)
