from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .container_probe_http_scheme import ContainerProbeHttpScheme
from .container_group_probe_http_headers_2 import ContainerGroupProbeHttpHeaders2


@JsonMap({})
class ContainerGroupProbeHttp(BaseModel):
    """ContainerGroupProbeHttp

    :param path: path
    :type path: str
    :param port: port
    :type port: int
    :param scheme: scheme, defaults to None
    :type scheme: ContainerProbeHttpScheme, optional
    :param headers: headers, defaults to None
    :type headers: List[ContainerGroupProbeHttpHeaders2], optional
    """

    def __init__(
        self,
        path: str,
        port: int,
        scheme: ContainerProbeHttpScheme = None,
        headers: List[ContainerGroupProbeHttpHeaders2] = None,
    ):
        """ContainerGroupProbeHttp

        :param path: path
        :type path: str
        :param port: port
        :type port: int
        :param scheme: scheme, defaults to None
        :type scheme: ContainerProbeHttpScheme, optional
        :param headers: headers, defaults to None
        :type headers: List[ContainerGroupProbeHttpHeaders2], optional
        """
        self.path = path
        self.port = self._define_number("port", port, ge=0, le=65536)
        self.scheme = (
            self._enum_matching(scheme, ContainerProbeHttpScheme.list(), "scheme")
            if scheme
            else None
        )
        self.headers = self._define_list(headers, ContainerGroupProbeHttpHeaders2)
