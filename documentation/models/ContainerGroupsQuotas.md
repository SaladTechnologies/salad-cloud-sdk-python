# ContainerGroupsQuotas

Represents the organization quotas for container groups

**Properties**

| Name                                         | Type | Required | Description                                                              |
| :------------------------------------------- | :--- | :------- | :----------------------------------------------------------------------- |
| container_replicas_quota                     | int  | ✅       | The maximum number of replicas that can be created for a container group |
| container_replicas_used                      | int  | ✅       | The number of replicas that are currently in use                         |
| max_container_group_reallocations_per_minute | int  | ❌       | The maximum number of container group reallocations per minute           |
| max_container_group_recreates_per_minute     | int  | ❌       | The maximum number of container group recreates per minute               |
| max_container_group_restarts_per_minute      | int  | ❌       | The maximum number of container group restarts per minute                |
