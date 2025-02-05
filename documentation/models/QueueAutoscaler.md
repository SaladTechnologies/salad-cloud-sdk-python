# QueueAutoscaler

Represents the autoscaling rules for a queue

**Properties**

| Name                     | Type | Required | Description                                                     |
| :----------------------- | :--- | :------- | :-------------------------------------------------------------- |
| min_replicas             | int  | ✅       | The minimum number of instances the container can scale down to |
| max_replicas             | int  | ✅       | The maximum number of instances the container can scale up to   |
| desired_queue_length     | int  | ✅       |                                                                 |
| polling_period           | int  | ❌       | The period (in seconds) in which the queue checks the formula   |
| max_upscale_per_minute   | int  | ❌       | The maximum number of instances that can be added per minute    |
| max_downscale_per_minute | int  | ❌       | The maximum number of instances that can be removed per minute  |
