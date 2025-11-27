# GpuClass

Represents a GPU Class

**Properties**

| Name           | Type                                    | Required | Description                                          |
| :------------- | :-------------------------------------- | :------- | :--------------------------------------------------- |
| id\_           | str                                     | ✅       | The unique identifier                                |
| name           | str                                     | ✅       | The GPU class name                                   |
| prices         | List[[GpuClassPrice](GpuClassPrice.md)] | ✅       | The list of prices for each container group priority |
| is_high_demand | bool                                    | ❌       | Whether the GPU class is in high demand              |
| gpu_class_type | GpuClassType                            | ❌       | The type of GPU class                                |
| gpu_count      | int                                     | ❌       | The number of GPUs in the cluster                    |
| min_vcpu       | int                                     | ❌       | The minimum vCPU count                               |
| max_vcpu       | int                                     | ❌       | The maximum vCPU count                               |
| min_ram        | int                                     | ❌       | The minimum RAM amount in MB                         |
| max_ram        | int                                     | ❌       | The maximum RAM amount in MB                         |
| min_storage    | int                                     | ❌       | The minimum storage amount in bytes                  |
| max_storage    | int                                     | ❌       | The maximum storage amount in bytes                  |

# GpuClassType

The type of GPU class

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| COMMUNITY | str  | ✅       | "community" |
| SECURE    | str  | ✅       | "secure"    |
