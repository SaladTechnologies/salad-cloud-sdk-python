# ContainerGroupInstanceStatusCount

A summary of container group instances categorized by their current lifecycle status

**Properties**

| Name             | Type | Required | Description                                                                    |
| :--------------- | :--- | :------- | :----------------------------------------------------------------------------- |
| allocating_count | int  | ✅       | The number of container instances that are currently being allocated resources |
| creating_count   | int  | ✅       | The number of container instances that are in the process of being created     |
| running_count    | int  | ✅       | The number of container instances that are currently running and operational   |
| stopping_count   | int  | ✅       | The number of container instances that are in the process of stopping          |
