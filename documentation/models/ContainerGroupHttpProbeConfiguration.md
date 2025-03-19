# ContainerGroupHttpProbeConfiguration

Defines HTTP probe configuration for container health checks within a container group.

**Properties**

| Name    | Type                                | Required | Description                                                                                                                                                                        |
| :------ | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| headers | List[ContainerGroupProbeHttpHeader] | ✅       | A collection of HTTP header name-value pairs used for configuring requests and responses in container group endpoints. Each header consists of a name and its corresponding value. |
| path    | str                                 | ✅       | The HTTP path that will be probed to check container health.                                                                                                                       |
| port    | int                                 | ✅       | The TCP port number to which the HTTP request will be sent.                                                                                                                        |
| scheme  | HttpScheme                          | ✅       | The protocol scheme used for HTTP probe requests in container health checks.                                                                                                       |
