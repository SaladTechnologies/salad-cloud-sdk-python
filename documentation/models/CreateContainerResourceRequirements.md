# CreateContainerResourceRequirements

Specifies the resource requirements for creating a container.

**Properties**

| Name           | Type      | Required | Description                                                                                                                                            |
| :------------- | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| cpu            | int       | ✅       | The number of CPU cores to allocate to the container (between 1 and 1024).                                                                             |
| memory         | int       | ✅       | The amount of memory to allocate to the container in megabytes (between 1024 and 1073741824).                                                          |
| gpu_classes    | List[str] | ❌       | A list of GPU class UUIDs required by the container. Can be null if no GPU is required.                                                                |
| storage_amount | int       | ❌       | The amount of storage to allocate to the container in bytes (between 1 GB and 1 PB).                                                                   |
| shm_size       | int       | ❌       | The amount of shared memory to allocate to the container via `/dev/shm` in megabytes (between 64 and 1073741824). If not specified, defaults to 64 MB. |
