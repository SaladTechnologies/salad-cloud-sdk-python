# CreateContainerGroup

Represents a request to create a container group

**Properties**

| Name             | Type                           | Required | Description                                                                                     |
| :--------------- | :----------------------------- | :------- | :---------------------------------------------------------------------------------------------- |
| name             | str                            | ✅       |                                                                                                 |
| container        | CreateContainer                | ✅       | Represents a container                                                                          |
| autostart_policy | bool                           | ✅       |                                                                                                 |
| restart_policy   | ContainerRestartPolicy         | ✅       |                                                                                                 |
| replicas         | int                            | ✅       |                                                                                                 |
| display_name     | str                            | ❌       |                                                                                                 |
| country_codes    | List[CountryCode]              | ❌       | List of countries nodes must be located in. Remove this field to permit nodes from any country. |
| networking       | CreateContainerGroupNetworking | ❌       | Represents container group networking parameters                                                |
| liveness_probe   | ContainerGroupLivenessProbe    | ❌       | Represents the container group liveness probe                                                   |
| readiness_probe  | ContainerGroupReadinessProbe   | ❌       | Represents the container group readiness probe                                                  |
| startup_probe    | ContainerGroupStartupProbe     | ❌       | Represents the container group startup probe                                                    |
| queue_connection | ContainerGroupQueueConnection  | ❌       | Represents container group queue connection                                                     |
| queue_autoscaler | QueueAutoscaler                | ❌       | Represents the autoscaling rules for a queue                                                    |
