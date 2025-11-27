# ContainerGroupState

Represents the operational state of a container group during its lifecycle, including timing information, status, and instance distribution metrics. This state captures the current execution status, start and finish times, and provides visibility into the operational health across instances.

**Properties**

| Name                   | Type                                                                      | Required | Description                                                                              |
| :--------------------- | :------------------------------------------------------------------------ | :------- | :--------------------------------------------------------------------------------------- |
| finish_time            | str                                                                       | ✅       | Timestamp when the container group execution finished or is expected to finish           |
| instance_status_counts | [ContainerGroupInstanceStatusCount](ContainerGroupInstanceStatusCount.md) | ✅       | A summary of container group instances categorized by their current lifecycle status     |
| start_time             | str                                                                       | ✅       | Timestamp when the container group execution started                                     |
| status                 | [ContainerGroupStatus](ContainerGroupStatus.md)                           | ✅       | Represents the current operational state of a container group within the Salad platform. |
| description            | str                                                                       | ❌       | Optional textual description or notes about the current state of the container group     |
