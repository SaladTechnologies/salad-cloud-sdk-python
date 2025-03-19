# ContainerGroupProbeExec

Defines the exec action for a probe in a container group. This is used to execute a command inside a container for health checks.

**Properties**

| Name    | Type      | Required | Description                                                                                                                          |
| :------ | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| command | List[str] | ✅       | The command to execute inside the container. Exit status of 0 is considered successful, any other exit status is considered failure. |
