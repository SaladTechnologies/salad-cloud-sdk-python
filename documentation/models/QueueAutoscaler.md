# QueueAutoscaler

Represents the autoscaling rules for a queue

**Properties**

| Name                     | Type | Required | Description |
| :----------------------- | :--- | :------- | :---------- |
| min_replicas             | int  | ✅       |             |
| max_replicas             | int  | ✅       |             |
| desired_queue_length     | int  | ✅       |             |
| polling_period           | int  | ❌       |             |
| max_upscale_per_minute   | int  | ❌       |             |
| max_downscale_per_minute | int  | ❌       |             |
