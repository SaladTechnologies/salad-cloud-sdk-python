# ContainerResourceUpdateSchema

Defines the resource specifications that can be modified for a container group, including CPU, memory, GPU classes, and storage allocations.

**Properties**

| Name           | Type      | Required | Description                                                                                  |
| :------------- | :-------- | :------- | :------------------------------------------------------------------------------------------- |
| cpu            | int       | ❌       | The number of CPU cores to allocate to the container (between 1 and 1024 cores).             |
| memory         | int       | ❌       | The amount of memory to allocate to the container in megabytes (between 1024MB and 1073741824MB). |
| gpu_classes    | List[str] | ❌       | List of GPU class identifiers that the container can use, specified as UUIDs.                |
| storage_amount | int       | ❌       | The amount of storage to allocate to the container in bytes (between 1 GB and 1 PB (1125899906842624 bytes)). |
| shm_size       | int       | ❌       | The size of the shared memory (/dev/shm) in MB. If not specified, defaults to 64MB.          |
