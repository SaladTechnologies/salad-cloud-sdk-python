# ContainerGroupNetworking

Represents container group networking parameters

**Properties**

| Name                    | Type                                 | Required | Description |
| :---------------------- | :----------------------------------- | :------- | :---------- |
| protocol                | ContainerNetworkingProtocol          | ✅       |             |
| port                    | int                                  | ✅       |             |
| auth                    | bool                                 | ✅       |             |
| dns                     | str                                  | ✅       |             |
| load_balancer           | ContainerGroupNetworkingLoadBalancer | ❌       |             |
| single_connection_limit | bool                                 | ❌       |             |
| client_request_timeout  | int                                  | ❌       |             |
| server_response_timeout | int                                  | ❌       |             |

# ContainerGroupNetworkingLoadBalancer

**Properties**

| Name                     | Type | Required | Description                   |
| :----------------------- | :--- | :------- | :---------------------------- |
| ROUNDROBIN               | str  | ✅       | "round_robin"                 |
| LEASTNUMBEROFCONNECTIONS | str  | ✅       | "least_number_of_connections" |
