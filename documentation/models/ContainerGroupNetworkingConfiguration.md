# ContainerGroupNetworkingConfiguration

Network configuration for container groups that defines connectivity, routing, and access control settings

**Properties**

| Name                    | Type                                    | Required | Description                                                                                                                                                       |
| :---------------------- | :-------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| auth                    | bool                                    | ✅       | Whether authentication is required for network access to the container group                                                                                      |
| dns                     | str                                     | ✅       | Domain name or URL endpoint for the container group's network interface                                                                                           |
| load_balancer           | TheContainerGroupNetworkingLoadBalancer | ✅       | The container group networking load balancer.                                                                                                                     |
| port                    | int                                     | ✅       | The container group networking port.                                                                                                                              |
| protocol                | ContainerNetworkingProtocol             | ✅       | Defines the communication protocol used for network traffic between containers or external systems. Currently supports HTTP protocol for web-based communication. |
| client_request_timeout  | int                                     | ❌       | The container group networking client request timeout.                                                                                                            |
| server_response_timeout | int                                     | ❌       | The container group networking server response timeout.                                                                                                           |
| single_connection_limit | bool                                    | ❌       | The container group networking single connection limit flag.                                                                                                      |
