# Queue

Represents a queue.

**Properties**

| Name                 | Type                                      | Required | Description                                                                                                                                                |
| :------------------- | :---------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| container_groups     | List[[ContainerGroup](ContainerGroup.md)] | ✅       | The container groups that are part of this queue. Each container group represents a scalable set of identical containers running as a distributed service. |
| create_time          | str                                       | ✅       | The date and time the queue was created.                                                                                                                   |
| display_name         | str                                       | ✅       | The display name. This may be used as a more human-readable name.                                                                                          |
| id\_                 | str                                       | ✅       | The queue identifier. This is automatically generated and assigned when the queue is created.                                                              |
| name                 | str                                       | ✅       | The queue name. This must be unique within the project.                                                                                                    |
| update_time          | str                                       | ✅       | The date and time the queue was last updated.                                                                                                              |
| current_queue_length | int                                       | ❌       | The current length of the queue                                                                                                                            |
| description          | str                                       | ❌       | The description. This may be used as a space for notes or other information about the queue.                                                               |
