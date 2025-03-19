# InferenceEndpointJobPrototype

Represents a request to create a inference endpoint job

**Properties**

| Name        | Type | Required | Description                                              |
| :---------- | :--- | :------- | :------------------------------------------------------- |
| input       | any  | ✅       | The job input. May be any valid JSON.                    |
| metadata    | dict | ❌       | The job metadata. May be any valid JSON.                 |
| webhook     | str  | ❌       | The webhook URL to which the job results will be POSTed. |
| webhook_url | str  | ❌       | The webhook URL to which the job results will be POSTed. |
