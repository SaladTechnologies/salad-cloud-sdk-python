# GpuAvailabilityPrototype

**Properties**

| Name           | Type                                | Required | Description                                               |
| :------------- | :---------------------------------- | :------- | :-------------------------------------------------------- |
| gpu_classes    | List[str]                           | ✅       | A list of available GPU class names                       |
| country_codes  | List[[CountryCode](CountryCode.md)] | ❌       | A list of country codes where the resources are available |
| cpu            | int                                 | ❌       | The number of available CPU cores                         |
| memory         | int                                 | ❌       | The amount of available memory in MB                      |
| storage_amount | int                                 | ❌       | The amount of available storage in bytes                  |
