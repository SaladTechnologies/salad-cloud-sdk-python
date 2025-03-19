# SystemLog

Represents a system log

**Properties**

| Name                    | Type | Required | Description                                       |
| :---------------------- | :--- | :------- | :------------------------------------------------ |
| event_name              | str  | ✅       | The name of the event                             |
| event_time              | str  | ✅       | The UTC date & time when the log item was created |
| resource_cpu            | int  | ✅       | The number of CPUs                                |
| resource_gpu_class      | str  | ✅       | The GPU class name                                |
| resource_memory         | int  | ✅       | The memory amount in MB                           |
| resource_storage_amount | int  | ✅       | The storage amount in bytes                       |
| version                 | str  | ✅       | The version instance ID                           |
| instance_id             | str  | ❌       | The container group instance identifier.          |
| machine_id              | str  | ❌       | The container group machine identifier.           |
