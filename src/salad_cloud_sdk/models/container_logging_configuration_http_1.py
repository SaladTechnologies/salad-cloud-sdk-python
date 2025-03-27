from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .container_logging_http_format import ContainerLoggingHttpFormat
from .container_logging_http_header import ContainerLoggingHttpHeader
from .container_logging_http_compression import ContainerLoggingHttpCompression


@JsonMap({})
class ContainerLoggingConfigurationHttp1(BaseModel):
    """Configuration for sending container logs to an HTTP endpoint. Defines how logs are formatted, compressed, and transmitted.

    :param host: The hostname or IP address of the HTTP logging endpoint
    :type host: str
    :param port: The port number of the HTTP logging endpoint (1-65535)
    :type port: int
    :param user: Optional username for HTTP authentication, defaults to None
    :type user: str, optional
    :param password: Optional password for HTTP authentication, defaults to None
    :type password: str, optional
    :param path: Optional URL path for the HTTP endpoint, defaults to None
    :type path: str, optional
    :param format: The format in which logs will be delivered
    :type format: ContainerLoggingHttpFormat
    :param headers: Optional HTTP headers to include in log transmission requests
    :type headers: List[ContainerLoggingHttpHeader]
    :param compression: The compression algorithm to apply to logs before transmission
    :type compression: ContainerLoggingHttpCompression
    """

    def __init__(
        self,
        host: str,
        port: int,
        format: ContainerLoggingHttpFormat,
        headers: Union[List[ContainerLoggingHttpHeader], None],
        compression: ContainerLoggingHttpCompression,
        user: Union[str, None] = SENTINEL,
        password: Union[str, None] = SENTINEL,
        path: Union[str, None] = SENTINEL,
        **kwargs,
    ):
        """Configuration for sending container logs to an HTTP endpoint. Defines how logs are formatted, compressed, and transmitted.

        :param host: The hostname or IP address of the HTTP logging endpoint
        :type host: str
        :param port: The port number of the HTTP logging endpoint (1-65535)
        :type port: int
        :param user: Optional username for HTTP authentication, defaults to None
        :type user: str, optional
        :param password: Optional password for HTTP authentication, defaults to None
        :type password: str, optional
        :param path: Optional URL path for the HTTP endpoint, defaults to None
        :type path: str, optional
        :param format: The format in which logs will be delivered
        :type format: ContainerLoggingHttpFormat
        :param headers: Optional HTTP headers to include in log transmission requests
        :type headers: List[ContainerLoggingHttpHeader]
        :param compression: The compression algorithm to apply to logs before transmission
        :type compression: ContainerLoggingHttpCompression
        """
        self.host = self._define_str(
            "host", host, pattern="^.*$", min_length=1, max_length=1000
        )
        self.port = self._define_number("port", port, ge=1, le=65535)
        if user is not SENTINEL:
            self.user = self._define_str(
                "user",
                user,
                nullable=True,
                pattern="^.*$",
                min_length=1,
                max_length=1000,
            )
        if password is not SENTINEL:
            self.password = self._define_str(
                "password",
                password,
                nullable=True,
                pattern="^.*$",
                min_length=1,
                max_length=1000,
            )
        if path is not SENTINEL:
            self.path = self._define_str(
                "path",
                path,
                nullable=True,
                pattern="^.*$",
                min_length=1,
                max_length=1000,
            )
        self.format = self._enum_matching(
            format, ContainerLoggingHttpFormat.list(), "format"
        )
        self.headers = self._define_list(headers, ContainerLoggingHttpHeader)
        self.compression = self._enum_matching(
            compression, ContainerLoggingHttpCompression.list(), "compression"
        )
        self._kwargs = kwargs
