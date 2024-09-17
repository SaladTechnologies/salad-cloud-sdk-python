# ContainerGroupState

Represents a container group state

**Properties**

| Name                   | Type                              | Required | Description                                        |
| :--------------------- | :-------------------------------- | :------- | :------------------------------------------------- |
| status                 | ContainerGroupStatus              | ✅       |                                                    |
| start_time             | str                               | ✅       |                                                    |
| finish_time            | str                               | ✅       |                                                    |
| instance_status_counts | ContainerGroupInstanceStatusCount | ✅       | Represents a container group instance status count |
| description            | str                               | ❌       |                                                    |
