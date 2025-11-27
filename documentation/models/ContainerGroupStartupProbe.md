# ContainerGroupStartupProbe

Defines a probe that checks if a container application has started successfully. Startup probes help prevent applications from being prematurely marked as unhealthy during initialization. The probe can use HTTP requests, TCP connections, gRPC calls, or shell commands to determine startup status.

**Properties**

| Name                  | Type                                                                            | Required | Description                                                                                                                       |
| :-------------------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| failure_threshold     | int                                                                             | ✅       | Number of times the probe must fail before considering the container not started                                                  |
| initial_delay_seconds | int                                                                             | ✅       | Number of seconds to wait after container startup before the first probe is executed                                              |
| period_seconds        | int                                                                             | ✅       | How frequently (in seconds) to perform the probe                                                                                  |
| success_threshold     | int                                                                             | ✅       | Minimum consecutive successes required for the probe to be considered successful                                                  |
| timeout_seconds       | int                                                                             | ✅       | Maximum time (in seconds) to wait for a probe response before considering it failed                                               |
| exec\_                | [ContainerGroupProbeExec](ContainerGroupProbeExec.md)                           | ❌       | Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks. |
| grpc                  | [ContainerGroupGRpcProbe](ContainerGroupGRpcProbe.md)                           | ❌       | Configuration for gRPC-based health probes in container groups, used to determine container health status.                        |
| http                  | [ContainerGroupHttpProbeConfiguration](ContainerGroupHttpProbeConfiguration.md) | ❌       | Defines HTTP probe configuration for container health checks within a container group.                                            |
| tcp                   | [ContainerGroupTcpProbe](ContainerGroupTcpProbe.md)                             | ❌       | Configuration for a TCP probe used to check container health via network connectivity.                                            |
