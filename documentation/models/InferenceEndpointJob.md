# InferenceEndpointJob

Represents a inference endpoint job

**Properties**

| Name                    | Type                            | Required | Description                                    |
| :---------------------- | :------------------------------ | :------- | :--------------------------------------------- |
| id\_                    | str                             | ✅       | The unique identifier.                         |
| input                   | any                             | ✅       | The job input. May be any valid JSON.          |
| inference_endpoint_name | str                             | ✅       | The inference endpoint name.                   |
| status                  | InferenceEndpointJobStatus      | ✅       | The current status.                            |
| events                  | List[InferenceEndpointJobEvent] | ✅       | The list of events.                            |
| organization_name       | str                             | ✅       | The organization name.                         |
| create_time             | str                             | ✅       | The time the job was created.                  |
| update_time             | str                             | ✅       | The time the job was last updated.             |
| metadata                | dict                            | ❌       | The job metadata. May be any valid JSON.       |
| webhook                 | str                             | ❌       | The webhook URL called when the job completes. |
| output                  | any                             | ❌       | The job output. May be any valid JSON.         |

# InferenceEndpointJobStatus

The current status.

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| PENDING   | str  | ✅       | "pending"   |
| RUNNING   | str  | ✅       | "running"   |
| SUCCEEDED | str  | ✅       | "succeeded" |
| CANCELLED | str  | ✅       | "cancelled" |
| FAILED    | str  | ✅       | "failed"    |
