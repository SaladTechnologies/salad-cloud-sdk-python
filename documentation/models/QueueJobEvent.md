# QueueJobEvent

Represents an event for queue job

**Properties**

| Name   | Type   | Required | Description                                    |
| :----- | :----- | :------- | :--------------------------------------------- |
| action | Action | ✅       | The action that was taken on the queue job     |
| time   | str    | ✅       | The time the action was taken on the queue job |

# Action

The action that was taken on the queue job

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| CREATED   | str  | ✅       | "created"   |
| STARTED   | str  | ✅       | "started"   |
| SUCCEEDED | str  | ✅       | "succeeded" |
| CANCELLED | str  | ✅       | "cancelled" |
| FAILED    | str  | ✅       | "failed"    |
