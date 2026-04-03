# QueueJob

Represents a queue job

**Properties**

| Name        | Type                                    | Required | Description                                      |
| :---------- | :-------------------------------------- | :------- | :----------------------------------------------- |
| create_time | str                                     | ✅       | The job creation time                            |
| events      | List[[QueueJobEvent](QueueJobEvent.md)] | ✅       | The job events                                   |
| id\_        | str                                     | ✅       | The job identifier                               |
| input       | any                                     | ✅       | The job input. May be any valid JSON.            |
| status      | QueueJobStatus                          | ✅       | The job status                                   |
| update_time | str                                     | ✅       | The job update time                              |
| metadata    | dict                                    | ❌       | Additional metadata for the job                  |
| output      | any                                     | ❌       | The job output. May be any valid JSON.           |
| webhook     | str                                     | ❌       | The webhook URL to notify when the job completes |

# QueueJobStatus

The job status

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| PENDING   | str  | ✅       | "pending"   |
| RUNNING   | str  | ✅       | "running"   |
| SUCCEEDED | str  | ✅       | "succeeded" |
| CANCELLED | str  | ✅       | "cancelled" |
| FAILED    | str  | ✅       | "failed"    |
