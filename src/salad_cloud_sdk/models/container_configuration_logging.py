from __future__ import annotations
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .axiom_logging_configuration import AxiomLoggingConfiguration
from .datadog_logging_configuration import DatadogLoggingConfiguration
from .container_logging_configuration_http_2 import ContainerLoggingConfigurationHttp2
from .new_relic_logging_configuration import NewRelicLoggingConfiguration
from .container_logging_splunk_configuration import ContainerLoggingSplunkConfiguration
from .tcp_logging_configuration import TcpLoggingConfiguration


@JsonMap({})
class ContainerConfigurationLogging(BaseModel):
    """Configuration options for directing container logs to a logging provider. This schema enables you to specify a single logging destination for container output, supporting monitoring, debugging, and analytics use cases. Each provider has its own configuration parameters defined in the referenced schemas. Only one logging provider can be selected at a time.

    :param axiom: Configuration settings for integrating container logs with the Axiom logging service. When specified, container logs will be forwarded to the Axiom instance defined by these parameters., defaults to None
    :type axiom: AxiomLoggingConfiguration, optional
    :param datadog: Configuration for forwarding container logs to Datadog monitoring service., defaults to None
    :type datadog: DatadogLoggingConfiguration, optional
    :param http: Configuration for sending container logs to an HTTP endpoint. Defines how logs are formatted, compressed, and transmitted., defaults to None
    :type http: ContainerLoggingConfigurationHttp2, optional
    :param new_relic: Configuration for sending container logs to New Relic's log management platform., defaults to None
    :type new_relic: NewRelicLoggingConfiguration, optional
    :param splunk: Configuration settings for forwarding container logs to a Splunk instance., defaults to None
    :type splunk: ContainerLoggingSplunkConfiguration, optional
    :param tcp: Configuration for forwarding container logs to a remote TCP endpoint, defaults to None
    :type tcp: TcpLoggingConfiguration, optional
    """

    def __init__(
        self,
        axiom: AxiomLoggingConfiguration = SENTINEL,
        datadog: DatadogLoggingConfiguration = SENTINEL,
        http: ContainerLoggingConfigurationHttp2 = SENTINEL,
        new_relic: NewRelicLoggingConfiguration = SENTINEL,
        splunk: ContainerLoggingSplunkConfiguration = SENTINEL,
        tcp: TcpLoggingConfiguration = SENTINEL,
        **kwargs,
    ):
        """Configuration options for directing container logs to a logging provider. This schema enables you to specify a single logging destination for container output, supporting monitoring, debugging, and analytics use cases. Each provider has its own configuration parameters defined in the referenced schemas. Only one logging provider can be selected at a time.

        :param axiom: Configuration settings for integrating container logs with the Axiom logging service. When specified, container logs will be forwarded to the Axiom instance defined by these parameters., defaults to None
        :type axiom: AxiomLoggingConfiguration, optional
        :param datadog: Configuration for forwarding container logs to Datadog monitoring service., defaults to None
        :type datadog: DatadogLoggingConfiguration, optional
        :param http: Configuration for sending container logs to an HTTP endpoint. Defines how logs are formatted, compressed, and transmitted., defaults to None
        :type http: ContainerLoggingConfigurationHttp2, optional
        :param new_relic: Configuration for sending container logs to New Relic's log management platform., defaults to None
        :type new_relic: NewRelicLoggingConfiguration, optional
        :param splunk: Configuration settings for forwarding container logs to a Splunk instance., defaults to None
        :type splunk: ContainerLoggingSplunkConfiguration, optional
        :param tcp: Configuration for forwarding container logs to a remote TCP endpoint, defaults to None
        :type tcp: TcpLoggingConfiguration, optional
        """
        if axiom is not SENTINEL:
            self.axiom = self._define_object(axiom, AxiomLoggingConfiguration)
        if datadog is not SENTINEL:
            self.datadog = self._define_object(datadog, DatadogLoggingConfiguration)
        if http is not SENTINEL:
            self.http = self._define_object(http, ContainerLoggingConfigurationHttp2)
        if new_relic is not SENTINEL:
            self.new_relic = self._define_object(
                new_relic, NewRelicLoggingConfiguration
            )
        if splunk is not SENTINEL:
            self.splunk = self._define_object(
                splunk, ContainerLoggingSplunkConfiguration
            )
        if tcp is not SENTINEL:
            self.tcp = self._define_object(tcp, TcpLoggingConfiguration)
        self._kwargs = kwargs
