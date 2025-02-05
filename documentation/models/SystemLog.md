# SystemLog

Represents a system log

**Properties**

| Name                    | Type | Required | Description                                       |
| :---------------------- | :--- | :------- | :------------------------------------------------ |
| event_name              | str  | ✅       | The name of the event                             |
| event_time              | str  | ✅       | The UTC date & time when the log item was created |
| version                 | str  | ✅       | The version instance ID                           |
| resource_cpu            | int  | ✅       | The number of CPUs                                |
| resource_memory         | int  | ✅       | The memory amount in MB                           |
| resource_gpu_class      | str  | ✅       | The GPU class name                                |
| resource_storage_amount | int  | ✅       | The storage amount in bytes                       |
| instance_id             | str  | ❌       | The unique instance ID                            |
| machine_id              | str  | ❌       | The organization-specific machine ID              |
