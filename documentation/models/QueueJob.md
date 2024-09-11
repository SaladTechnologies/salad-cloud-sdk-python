# QueueJob

Represents a queue job

**Properties**

| Name        | Type                  | Required | Description                            |
| :---------- | :-------------------- | :------- | :------------------------------------- |
| id\_        | `str`                 | ✅       |                                        |
| input       | `any`                 | ✅       | The job input. May be any valid JSON.  |
| status      | `QueueJobStatus`      | ✅       |                                        |
| events      | `List[QueueJobEvent]` | ✅       |                                        |
| create_time | `str`                 | ✅       |                                        |
| update_time | `str`                 | ✅       |                                        |
| metadata    | `dict`                | ❌       |                                        |
| webhook     | `str`                 | ❌       |                                        |
| output      | `any`                 | ❌       | The job output. May be any valid JSON. |

# QueueJobStatus

**Properties**

| Name      | Type  | Required | Description |
| :-------- | :---- | :------- | :---------- |
| PENDING   | `str` | ✅       | "pending"   |
| RUNNING   | `str` | ✅       | "running"   |
| SUCCEEDED | `str` | ✅       | "succeeded" |
| CANCELLED | `str` | ✅       | "cancelled" |
| FAILED    | `str` | ✅       | "failed"    |
