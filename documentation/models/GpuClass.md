# GpuClass

Represents a GPU Class

**Properties**

| Name           | Type                  | Required | Description                                          |
| :------------- | :-------------------- | :------- | :--------------------------------------------------- |
| id\_           | `str`                 | ✅       | The unique identifier                                |
| name           | `str`                 | ✅       | The GPU class name                                   |
| prices         | `List[GpuClassPrice]` | ✅       | The list of prices for each container group priority |
| is_high_demand | `bool`                | ❌       | Whether the GPU class is in high demand              |
