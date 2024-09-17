# UpdateContainerGroup

Represents a request to update a container group

**Properties**

| Name            | Type                           | Required | Description                                                                                     |
| :-------------- | :----------------------------- | :------- | :---------------------------------------------------------------------------------------------- |
| display_name    | str                            | ❌       |                                                                                                 |
| container       | UpdateContainer                | ❌       | Represents an update container object                                                           |
| replicas        | int                            | ❌       |                                                                                                 |
| country_codes   | List[CountryCode]              | ❌       | List of countries nodes must be located in. Remove this field to permit nodes from any country. |
| networking      | UpdateContainerGroupNetworking | ❌       | Represents update container group networking parameters                                         |
| liveness_probe  | ContainerGroupLivenessProbe    | ❌       | Represents the container group liveness probe                                                   |
| readiness_probe | ContainerGroupReadinessProbe   | ❌       | Represents the container group readiness probe                                                  |
| startup_probe   | ContainerGroupStartupProbe     | ❌       | Represents the container group startup probe                                                    |
