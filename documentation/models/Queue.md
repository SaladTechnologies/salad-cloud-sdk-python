# Queue

Represents a queue

**Properties**

| Name             | Type                 | Required | Description     |
| :--------------- | :------------------- | :------- | :-------------- |
| id\_             | str                  | ✅       |                 |
| name             | str                  | ✅       |                 |
| display_name     | str                  | ✅       |                 |
| container_groups | List[ContainerGroup] | ✅       |                 |
| create_time      | str                  | ✅       |                 |
| update_time      | str                  | ✅       |                 |
| description      | str                  | ❌       | The description |
