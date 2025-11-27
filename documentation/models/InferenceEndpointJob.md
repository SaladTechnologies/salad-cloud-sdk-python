# InferenceEndpointJob

Represents a inference endpoint job

**Properties**

| Name                    | Type                                                            | Required | Description                                    |
| :---------------------- | :-------------------------------------------------------------- | :------- | :--------------------------------------------- |
| id\_                    | str                                                             | ✅       | The inference endpoint job identifier.         |
| inference_endpoint_name | str                                                             | ✅       | The inference endpoint name.                   |
| organization_name       | str                                                             | ✅       | The organization name.                         |
| input                   | any                                                             | ✅       | The job input. May be any valid JSON.          |
| status                  | [Status](Status.md)                                             | ✅       | The current status.                            |
| events                  | List[[InferenceEndpointJobEvent](InferenceEndpointJobEvent.md)] | ✅       | The list of events.                            |
| create_time             | str                                                             | ✅       | The time the job was created.                  |
| update_time             | str                                                             | ✅       | The time the job was last updated.             |
| metadata                | dict                                                            | ❌       | The job metadata. May be any valid JSON.       |
| webhook                 | str                                                             | ❌       | The webhook URL called when the job completes. |
| webhook_url             | str                                                             | ❌       | The webhook URL called when the job completes. |
| output                  | any                                                             | ❌       | The job output. May be any valid JSON.         |
