# WorkloadError

Represents a workload error

**Properties**

| Name         | Type | Required | Description                                                                             |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------- |
| allocated_at | str  | ✅       | The timestamp when the workload was initially allocated to a machine                    |
| detail       | str  | ✅       | A detailed error message describing the nature and cause of the workload failure        |
| failed_at    | str  | ✅       | The timestamp when the workload failure was detected or reported                        |
| instance_id  | str  | ✅       | The container group instance identifier.                                                |
| machine_id   | str  | ✅       | The container group machine identifier.                                                 |
| version      | int  | ✅       | The schema version number for this error record, used for tracking error format changes |
| started_at   | str  | ❌       | The timestamp when the workload started execution, or null if it failed before starting |
