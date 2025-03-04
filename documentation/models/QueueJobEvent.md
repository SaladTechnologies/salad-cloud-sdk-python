# QueueJobEvent

Represents an event for queue job

**Properties**

| Name   | Type   | Required | Description |
| :----- | :----- | :------- | :---------- |
| action | Action | ✅       |             |
| time   | str    | ✅       |             |

# Action

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| CREATED   | str  | ✅       | "created"   |
| STARTED   | str  | ✅       | "started"   |
| SUCCEEDED | str  | ✅       | "succeeded" |
| CANCELLED | str  | ✅       | "cancelled" |
| FAILED    | str  | ✅       | "failed"    |
