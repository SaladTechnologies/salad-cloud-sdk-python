# ContainerGroup

Represents a container group

**Properties**

| Name             | Type                            | Required | Description                                                                                     |
| :--------------- | :------------------------------ | :------- | :---------------------------------------------------------------------------------------------- |
| id\_             | `str`                           | ✅       |                                                                                                 |
| name             | `str`                           | ✅       |                                                                                                 |
| display_name     | `str`                           | ✅       |                                                                                                 |
| container        | `Container`                     | ✅       | Represents a container                                                                          |
| autostart_policy | `bool`                          | ✅       |                                                                                                 |
| restart_policy   | `ContainerRestartPolicy`        | ✅       |                                                                                                 |
| replicas         | `int`                           | ✅       |                                                                                                 |
| current_state    | `ContainerGroupState`           | ✅       | Represents a container group state                                                              |
| create_time      | `str`                           | ✅       |                                                                                                 |
| update_time      | `str`                           | ✅       |                                                                                                 |
| pending_change   | `bool`                          | ✅       |                                                                                                 |
| version          | `int`                           | ✅       |                                                                                                 |
| country_codes    | `List[CountryCode]`             | ❌       | List of countries nodes must be located in. Remove this field to permit nodes from any country. |
| networking       | `ContainerGroupNetworking`      | ❌       | Represents container group networking parameters                                                |
| liveness_probe   | `ContainerGroupLivenessProbe`   | ❌       | Represents the container group liveness probe                                                   |
| readiness_probe  | `ContainerGroupReadinessProbe`  | ❌       | Represents the container group readiness probe                                                  |
| startup_probe    | `ContainerGroupStartupProbe`    | ❌       | Represents the container group startup probe                                                    |
| queue_connection | `ContainerGroupQueueConnection` | ❌       | Represents container group queue connection                                                     |
| queue_autoscaler | `QueueAutoscaler`               | ❌       | Represents the autoscaling rules for a queue                                                    |
