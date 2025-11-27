# GpuClassPrice

Represents the price of a GPU class for a given container group priority

**Properties**

| Name     | Type                                                | Required | Description                                                                                                                 |
| :------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------- |
| priority | [ContainerGroupPriority](ContainerGroupPriority.md) | ✅       | Specifies the priority level for container group execution, which determines resource allocation and scheduling precedence. |
| price    | str                                                 | ✅       | The price                                                                                                                   |
