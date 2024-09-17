# ContainerGroupInstance

Represents the details of a single container group instance

**Properties**

| Name        | Type  | Required | Description                                                                                                                                            |
| :---------- | :---- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| instance_id | str   | ✅       | The unique instance ID                                                                                                                                 |
| machine_id  | str   | ✅       | The machine ID                                                                                                                                         |
| state       | State | ✅       | The state of the container group instance                                                                                                              |
| update_time | str   | ✅       | The UTC date & time when the workload on this machine transitioned to the current state                                                                |
| version     | int   | ✅       | The version of the running container group                                                                                                             |
| ready       | bool  | ❌       | Specifies whether the container group instance is currently passing its readiness check. If no readiness probe is defined, is true once fully started. |
| started     | bool  | ❌       | Specifies whether the container group instance passed its startup probe. Is always true when no startup probe is defined.                              |

# State

The state of the container group instance

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| ALLOCATING  | str  | ✅       | "allocating"  |
| DOWNLOADING | str  | ✅       | "downloading" |
| CREATING    | str  | ✅       | "creating"    |
| RUNNING     | str  | ✅       | "running"     |
| STOPPING    | str  | ✅       | "stopping"    |
