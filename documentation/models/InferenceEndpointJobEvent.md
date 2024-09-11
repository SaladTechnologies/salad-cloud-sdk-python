# InferenceEndpointJobEvent

Represents an event for inference endpoint job

**Properties**

| Name   | Type                              | Required | Description |
| :----- | :-------------------------------- | :------- | :---------- |
| action | `InferenceEndpointJobEventAction` | ✅       |             |
| time   | `str`                             | ✅       |             |

# InferenceEndpointJobEventAction

**Properties**

| Name      | Type  | Required | Description |
| :-------- | :---- | :------- | :---------- |
| CREATED   | `str` | ✅       | "created"   |
| STARTED   | `str` | ✅       | "started"   |
| SUCCEEDED | `str` | ✅       | "succeeded" |
| CANCELLED | `str` | ✅       | "cancelled" |
| FAILED    | `str` | ✅       | "failed"    |
