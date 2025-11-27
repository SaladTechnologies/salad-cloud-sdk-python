# ContainerGroupLivenessProbe

Defines a liveness probe for container groups that determines when to restart a container if it becomes unhealthy

**Properties**

| Name                  | Type                                                                            | Required | Description                                                                                                                       |
| :-------------------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| failure_threshold     | int                                                                             | ✅       | Number of consecutive failures required to consider the probe as failed                                                           |
| initial_delay_seconds | int                                                                             | ✅       | Number of seconds to wait after container start before initiating liveness probes                                                 |
| period_seconds        | int                                                                             | ✅       | Frequency in seconds at which the probe should be executed                                                                        |
| success_threshold     | int                                                                             | ✅       | Number of consecutive successes required to consider the probe successful                                                         |
| timeout_seconds       | int                                                                             | ✅       | Number of seconds after which the probe times out if no response is received                                                      |
| exec\_                | [ContainerGroupProbeExec](ContainerGroupProbeExec.md)                           | ❌       | Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks. |
| grpc                  | [ContainerGroupGRpcProbe](ContainerGroupGRpcProbe.md)                           | ❌       | Configuration for gRPC-based health probes in container groups, used to determine container health status.                        |
| http                  | [ContainerGroupHttpProbeConfiguration](ContainerGroupHttpProbeConfiguration.md) | ❌       | Defines HTTP probe configuration for container health checks within a container group.                                            |
| tcp                   | [ContainerGroupTcpProbe](ContainerGroupTcpProbe.md)                             | ❌       | Configuration for a TCP probe used to check container health via network connectivity.                                            |
