# CreateContainerGroupNetworking

Represents container group networking parameters

**Properties**

| Name                    | Type                                       | Required | Description |
| :---------------------- | :----------------------------------------- | :------- | :---------- |
| protocol                | ContainerNetworkingProtocol                | ✅       |             |
| port                    | int                                        | ✅       |             |
| auth                    | bool                                       | ✅       |             |
| load_balancer           | CreateContainerGroupNetworkingLoadBalancer | ❌       |             |
| single_connection_limit | bool                                       | ❌       |             |
| client_request_timeout  | int                                        | ❌       |             |
| server_response_timeout | int                                        | ❌       |             |

# CreateContainerGroupNetworkingLoadBalancer

**Properties**

| Name                     | Type | Required | Description                   |
| :----------------------- | :--- | :------- | :---------------------------- |
| ROUNDROBIN               | str  | ✅       | "round_robin"                 |
| LEASTNUMBEROFCONNECTIONS | str  | ✅       | "least_number_of_connections" |
