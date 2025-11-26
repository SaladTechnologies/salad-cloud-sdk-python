# ContainerResourceRequirements

Specifies the resource requirements for a container.

**Properties**

| Name           | Type      | Required | Description                                                                                                                          |
| :------------- | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| cpu            | int       | ✅       | The number of CPU cores required by the container. Must be between 1 and 1024.                                                       |
| memory         | int       | ✅       | The amount of memory (in MB) required by the container. Must be between 1024 MB and 1073741824 MB.                                   |
| gpu_classes    | List[str] | ✅       | A list of GPU class UUIDs required by the container. Can be null if no GPU is required.                                              |
| storage_amount | int       | ❌       | The amount of storage (in bytes) required by the container. Must be between 1 GB (1073741824 bytes) and 1 PB (1125899906842624 bytes). |
| shm_size       | int       | ❌       | The size of the shared memory (/dev/shm) in MB. If not specified, defaults to 64MB.                                                  |
