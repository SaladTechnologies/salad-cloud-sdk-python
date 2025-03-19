from __future__ import annotations
from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_group_probe_http_header import ContainerGroupProbeHttpHeader
from .http_scheme import HttpScheme


@JsonMap({})
class ContainerGroupHttpProbeConfiguration(BaseModel):
    """Defines HTTP probe configuration for container health checks within a container group.

    :param headers: A collection of HTTP header name-value pairs used for configuring requests and responses in container group endpoints. Each header consists of a name and its corresponding value.
    :type headers: List[ContainerGroupProbeHttpHeader]
    :param path: The HTTP path that will be probed to check container health.
    :type path: str
    :param port: The TCP port number to which the HTTP request will be sent.
    :type port: int
    :param scheme: The protocol scheme used for HTTP probe requests in container health checks.
    :type scheme: HttpScheme
    """

    def __init__(
        self,
        headers: List[ContainerGroupProbeHttpHeader],
        path: str,
        port: int,
        scheme: Union[HttpScheme, None],
        **kwargs,
    ):
        """Defines HTTP probe configuration for container health checks within a container group.

        :param headers: A collection of HTTP header name-value pairs used for configuring requests and responses in container group endpoints. Each header consists of a name and its corresponding value.
        :type headers: List[ContainerGroupProbeHttpHeader]
        :param path: The HTTP path that will be probed to check container health.
        :type path: str
        :param port: The TCP port number to which the HTTP request will be sent.
        :type port: int
        :param scheme: The protocol scheme used for HTTP probe requests in container health checks.
        :type scheme: HttpScheme
        """
        self.headers = self._define_list(headers, ContainerGroupProbeHttpHeader)
        self.path = self._define_str(
            "path", path, pattern="^.*$", min_length=1, max_length=2048
        )
        self.port = self._define_number("port", port, ge=0, le=65536)
        self.scheme = self._enum_matching(scheme, HttpScheme.list(), "scheme")
        self._kwargs = kwargs
