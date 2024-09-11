# ContainerGroupStartupProbe

Represents the container group startup probe

**Properties**

| Name                  | Type                      | Required | Description |
| :-------------------- | :------------------------ | :------- | :---------- |
| initial_delay_seconds | `int`                     | ✅       |             |
| period_seconds        | `int`                     | ✅       |             |
| timeout_seconds       | `int`                     | ✅       |             |
| success_threshold     | `int`                     | ✅       |             |
| failure_threshold     | `int`                     | ✅       |             |
| tcp                   | `ContainerGroupProbeTcp`  | ❌       |             |
| http                  | `ContainerGroupProbeHttp` | ❌       |             |
| grpc                  | `ContainerGroupProbeGrpc` | ❌       |             |
| exec\_                | `ContainerGroupProbeExec` | ❌       |             |
