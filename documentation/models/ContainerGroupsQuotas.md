# ContainerGroupsQuotas

**Properties**

| Name                                         | Type | Required | Description |
| :------------------------------------------- | :--- | :------- | :---------- |
| max_created_container_groups                 | int  | ✅       |             |
| container_instance_quota                     | int  | ✅       |             |
| max_container_group_reallocations_per_minute | int  | ❌       |             |
| max_container_group_recreates_per_minute     | int  | ❌       |             |
| max_container_group_restarts_per_minute      | int  | ❌       |             |
