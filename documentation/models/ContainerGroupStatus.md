# ContainerGroupStatus

Represents the current operational state of a container group within the Salad platform.

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| PENDING   | str  | ✅       | "pending"   |
| RUNNING   | str  | ✅       | "running"   |
| STOPPED   | str  | ✅       | "stopped"   |
| SUCCEEDED | str  | ✅       | "succeeded" |
| FAILED    | str  | ✅       | "failed"    |
| DEPLOYING | str  | ✅       | "deploying" |
