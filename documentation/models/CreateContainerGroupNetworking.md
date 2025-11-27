# CreateContainerGroupNetworking

Network configuration for container groups specifying connectivity parameters, including authentication, protocol, and timeout settings

**Properties**

| Name                    | Type                                                                                  | Required | Description                                                                                                                                                       |
| :---------------------- | :------------------------------------------------------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| auth                    | bool                                                                                  | ✅       | Determines whether authentication is required for network connections to the container group                                                                      |
| port                    | int                                                                                   | ✅       | The container group networking port.                                                                                                                              |
| protocol                | [ContainerNetworkingProtocol](ContainerNetworkingProtocol.md)                         | ✅       | Defines the communication protocol used for network traffic between containers or external systems. Currently supports HTTP protocol for web-based communication. |
| client_request_timeout  | int                                                                                   | ❌       | The container group networking client request timeout.                                                                                                            |
| load_balancer           | [TheContainerGroupNetworkingLoadBalancer](TheContainerGroupNetworkingLoadBalancer.md) | ❌       | The container group networking load balancer.                                                                                                                     |
| server_response_timeout | int                                                                                   | ❌       | The container group networking server response timeout.                                                                                                           |
| single_connection_limit | bool                                                                                  | ❌       | The container group networking single connection limit flag.                                                                                                      |
