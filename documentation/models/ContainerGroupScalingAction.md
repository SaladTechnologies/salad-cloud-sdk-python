# ContainerGroupScalingAction

Represents a scaling action configuration for a container group

**Properties**

| Name     | Type | Required | Description                                                           |
| :------- | :--- | :------- | :-------------------------------------------------------------------- |
| replicas | int  | ✅       | The number of replicas to scale to during the scheduled period        |
| schedule | str  | ✅       | The cron-style schedule string defining when the scaling should occur |
