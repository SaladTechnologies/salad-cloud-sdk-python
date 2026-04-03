# ContainerResourceUpdateSchema

Defines the resource specifications that can be modified for a container group, including CPU, memory, GPU classes, and storage allocations.

**Properties**

| Name           | Type      | Required | Description                                                                                                                                            |
| :------------- | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| cpu            | int       | ❌       | The number of CPU cores to allocate to the container (between 1 and 1024).                                                                             |
| gpu_classes    | List[str] | ❌       | List of GPU class identifiers that the container can use, specified as UUIDs.                                                                          |
| memory         | int       | ❌       | The amount of memory to allocate to the container in megabytes (between 1024 and 1073741824).                                                          |
| shm_size       | int       | ❌       | The amount of shared memory to allocate to the container via `/dev/shm` in megabytes (between 64 and 1073741824). If not specified, defaults to 64 MB. |
| storage_amount | int       | ❌       | The amount of storage to allocate to the container in bytes (between 1 GB and 1 PB).                                                                   |
