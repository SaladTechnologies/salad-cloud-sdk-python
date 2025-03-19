# ContainerGroupReadinessProbe

Defines how to check if a container is ready to serve traffic. The readiness probe determines whether the container's application is ready to accept traffic. If the readiness probe fails, the container is considered not ready and traffic will not be sent to it.

**Properties**

| Name                  | Type                                 | Required | Description                                                                                                                                                                                  |
| :-------------------- | :----------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| failure_threshold     | int                                  | ✅       | The number of consecutive failures required to consider the probe failed. After this many consecutive failures, the container is marked as not ready.                                        |
| initial_delay_seconds | int                                  | ✅       | The time in seconds to wait after the container starts before initiating the first probe. This allows time for the application to initialize before being tested.                            |
| period_seconds        | int                                  | ✅       | How frequently (in seconds) the probe should be executed during the container's lifetime. Specifies the interval between consecutive probe executions.                                       |
| success_threshold     | int                                  | ✅       | The minimum consecutive successes required to consider the probe successful after it has failed. Defines how many successful probe results are needed to transition from failure to success. |
| timeout_seconds       | int                                  | ✅       | The maximum time in seconds that the probe has to complete. If the probe doesn't return a result before the timeout, it's considered failed.                                                 |
| exec\_                | ContainerGroupProbeExec              | ❌       | Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks.                                                            |
| grpc                  | ContainerGroupGRpcProbe              | ❌       | Configuration for gRPC-based health probes in container groups, used to determine container health status.                                                                                   |
| http                  | ContainerGroupHttpProbeConfiguration | ❌       | Defines HTTP probe configuration for container health checks within a container group.                                                                                                       |
| tcp                   | ContainerGroupTcpProbe               | ❌       | Configuration for a TCP probe used to check container health via network connectivity.                                                                                                       |
