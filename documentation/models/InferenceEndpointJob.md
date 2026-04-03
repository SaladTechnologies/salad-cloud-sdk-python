# InferenceEndpointJob

Represents a inference endpoint job

**Properties**

| Name                    | Type                                                            | Required | Description                                    |
| :---------------------- | :-------------------------------------------------------------- | :------- | :--------------------------------------------- |
| create_time             | str                                                             | ✅       | The time the job was created.                  |
| events                  | List[[InferenceEndpointJobEvent](InferenceEndpointJobEvent.md)] | ✅       | The list of events.                            |
| id\_                    | str                                                             | ✅       | The inference endpoint job identifier.         |
| inference_endpoint_name | str                                                             | ✅       | The inference endpoint name.                   |
| input                   | any                                                             | ✅       | The job input. May be any valid JSON.          |
| organization_name       | str                                                             | ✅       | The organization name.                         |
| status                  | [Status](Status.md)                                             | ✅       | The current status.                            |
| update_time             | str                                                             | ✅       | The time the job was last updated.             |
| metadata                | dict                                                            | ❌       | The job metadata. May be any valid JSON.       |
| output                  | any                                                             | ❌       | The job output. May be any valid JSON.         |
| webhook                 | str                                                             | ❌       | The webhook URL called when the job completes. |
| webhook_url             | str                                                             | ❌       | The webhook URL called when the job completes. |
