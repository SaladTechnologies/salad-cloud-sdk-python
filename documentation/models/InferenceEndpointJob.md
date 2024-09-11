# InferenceEndpointJob

Represents a inference endpoint job

**Properties**

| Name                    | Type                              | Required | Description                            |
| :---------------------- | :-------------------------------- | :------- | :------------------------------------- |
| id\_                    | `str`                             | ✅       |                                        |
| input                   | `any`                             | ✅       | The job input. May be any valid JSON.  |
| inference_endpoint_name | `str`                             | ✅       | The inference endpoint name            |
| status                  | `InferenceEndpointJobStatus`      | ✅       |                                        |
| events                  | `List[InferenceEndpointJobEvent]` | ✅       |                                        |
| organization_name       | `str`                             | ✅       | The organization name                  |
| create_time             | `str`                             | ✅       |                                        |
| update_time             | `str`                             | ✅       |                                        |
| metadata                | `dict`                            | ❌       |                                        |
| webhook                 | `str`                             | ❌       |                                        |
| output                  | `any`                             | ❌       | The job output. May be any valid JSON. |

# InferenceEndpointJobStatus

**Properties**

| Name      | Type  | Required | Description |
| :-------- | :---- | :------- | :---------- |
| PENDING   | `str` | ✅       | "pending"   |
| RUNNING   | `str` | ✅       | "running"   |
| SUCCEEDED | `str` | ✅       | "succeeded" |
| CANCELLED | `str` | ✅       | "cancelled" |
| FAILED    | `str` | ✅       | "failed"    |
