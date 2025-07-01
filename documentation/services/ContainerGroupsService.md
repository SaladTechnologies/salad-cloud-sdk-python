# ContainerGroupsService

A list of all methods in the `ContainerGroupsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                                 |
| :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| [list_container_groups](#list_container_groups)                             | Gets the list of container groups                                                                                           |
| [create_container_group](#create_container_group)                           | Creates a new container group                                                                                               |
| [get_container_group](#get_container_group)                                 | Gets a container group                                                                                                      |
| [update_container_group](#update_container_group)                           | Updates a container group                                                                                                   |
| [delete_container_group](#delete_container_group)                           | Deletes a container group                                                                                                   |
| [start_container_group](#start_container_group)                             | Starts a container group                                                                                                    |
| [stop_container_group](#stop_container_group)                               | Stops a container group                                                                                                     |
| [list_container_group_instances](#list_container_group_instances)           | Gets the list of container group instances                                                                                  |
| [get_container_group_instance](#get_container_group_instance)               | Gets a container group instance                                                                                             |
| [update_container_group_instance](#update_container_group_instance)         | Updates a container group instance                                                                                          |
| [reallocate_container_group_instance](#reallocate_container_group_instance) | Reallocates a container group instance to run on a different Salad Node                                                     |
| [recreate_container_group_instance](#recreate_container_group_instance)     | Stops a container, destroys it, and starts a new one without requiring the image to be downloaded again on a new Salad Node |
| [restart_container_group_instance](#restart_container_group_instance)       | Stops a container and restarts it on the same Salad Node                                                                    |

## list_container_groups

Gets the list of container groups

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

**Return Type**

`ContainerGroupCollection`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.list_container_groups(
    organization_name="acme-corp",
    project_name="dev-env"
)

print(result)
```

## create_container_group

Creates a new container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers`

**Parameters**

| Name              | Type                                                                        | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [ContainerGroupCreationRequest](../models/ContainerGroupCreationRequest.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | str                                                                         | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str                                                                         | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

**Return Type**

`ContainerGroup`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import ContainerGroupCreationRequest

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = ContainerGroupCreationRequest(
    autostart_policy=False,
    container={
        "command": [
            "command"
        ],
        "environment_variables": {},
        "image": "acme/:latest",
        "image_caching": True,
        "logging": {
            "axiom": {
                "host": "host",
                "api_token": "api_token",
                "dataset": "dataset"
            },
            "datadog": {
                "host": "host",
                "api_key": "api_key",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "http": {
                "host": "host",
                "port": 29750,
                "user": "user",
                "password": "password",
                "path": "path",
                "format": "json",
                "headers": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ],
                "compression": "none"
            },
            "new_relic": {
                "host": "host",
                "ingestion_key": "ingestion_key"
            },
            "splunk": {
                "host": "host",
                "token": "token"
            },
            "tcp": {
                "host": "host",
                "port": 21602
            }
        },
        "priority": "high",
        "registry_authentication": {
            "aws_ecr": {
                "access_key_id": "access_key_id",
                "secret_access_key": "secret_access_key"
            },
            "basic": {
                "username": "username",
                "password": "password"
            },
            "docker_hub": {
                "username": "username",
                "personal_access_token": "personal_access_token"
            },
            "gcp_gar": {
                "service_key": "service_key"
            },
            "gcp_gcr": {
                "service_key": "service_key"
            }
        },
        "resources": {
            "cpu": 9,
            "memory": 61137,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 50129523289,
            "shm_size": 64
        }
    },
    country_codes=[
        "af"
    ],
    display_name="R81hlLvCDU",
    liveness_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 3,
        "grpc": {
            "port": 28667,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 53414,
            "scheme": "http"
        },
        "initial_delay_seconds": 67,
        "period_seconds": 10,
        "success_threshold": 1,
        "tcp": {
            "port": 62611
        },
        "timeout_seconds": 30
    },
    name="name",
    networking={
        "auth": True,
        "client_request_timeout": 100000,
        "load_balancer": "round_robin",
        "port": 60000,
        "protocol": "http",
        "server_response_timeout": 100000,
        "single_connection_limit": True
    },
    queue_autoscaler={
        "desired_queue_length": 22,
        "max_replicas": 462,
        "max_downscale_per_minute": 26,
        "max_upscale_per_minute": 52,
        "min_replicas": 82,
        "polling_period": 509
    },
    queue_connection={
        "path": "path",
        "port": 6006,
        "queue_name": "oxniyomose4errderfez5m6znpd3zgutjsc-eeb9"
    },
    readiness_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 3,
        "grpc": {
            "port": 28667,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 53414,
            "scheme": "http"
        },
        "initial_delay_seconds": 226,
        "period_seconds": 1,
        "success_threshold": 1,
        "tcp": {
            "port": 62611
        },
        "timeout_seconds": 1
    },
    replicas=490,
    restart_policy="always",
    startup_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 15,
        "grpc": {
            "port": 28667,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 53414,
            "scheme": "http"
        },
        "initial_delay_seconds": 1058,
        "tcp": {
            "port": 62611
        },
        "period_seconds": 3,
        "success_threshold": 2,
        "timeout_seconds": 10
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env"
)

print(result)
```

## get_container_group

Gets a container group

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |

**Return Type**

`ContainerGroup`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.get_container_group(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot"
)

print(result)
```

## update_container_group

Updates a container group

- HTTP Method: `PATCH`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type                                                    | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [ContainerGroupPatch](../models/ContainerGroupPatch.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name    | str                                                     | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str                                                     | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str                                                     | ✅       | The unique container group name                                                                                                                                                                                                                     |

**Return Type**

`ContainerGroup`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import ContainerGroupPatch

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = ContainerGroupPatch(
    display_name="e2ajyqqvL",
    container={
        "command": [
            "command"
        ],
        "environment_variables": {},
        "image": "image",
        "image_caching": True,
        "logging": {
            "axiom": {
                "host": "host",
                "api_token": "api_token",
                "dataset": "dataset"
            },
            "datadog": {
                "host": "host",
                "api_key": "api_key",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "http": {
                "host": "host",
                "port": 34677,
                "user": "user",
                "password": "password",
                "path": "path",
                "format": "json",
                "headers": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ],
                "compression": "none"
            },
            "new_relic": {
                "host": "host",
                "ingestion_key": "ingestion_key"
            },
            "splunk": {
                "host": "host",
                "token": "token"
            },
            "tcp": {
                "host": "host",
                "port": 21602
            }
        },
        "priority": "high",
        "registry_authentication": {
            "aws_ecr": {
                "access_key_id": "access_key_id",
                "secret_access_key": "secret_access_key"
            },
            "basic": {
                "username": "username",
                "password": "password"
            },
            "docker_hub": {
                "username": "username",
                "personal_access_token": "personal_access_token"
            },
            "gcp_gar": {
                "service_key": "service_key"
            },
            "gcp_gcr": {
                "service_key": "service_key"
            }
        },
        "resources": {
            "cpu": 2,
            "memory": 4272,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 47962159632,
            "shm_size": 64
        }
    },
    replicas=436,
    country_codes=[
        "af"
    ],
    networking={
        "port": 17663
    },
    liveness_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 3,
        "grpc": {
            "port": 28667,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 53414,
            "scheme": "http"
        },
        "initial_delay_seconds": 67,
        "period_seconds": 10,
        "success_threshold": 1,
        "tcp": {
            "port": 62611
        },
        "timeout_seconds": 30
    },
    readiness_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 3,
        "grpc": {
            "port": 28667,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 53414,
            "scheme": "http"
        },
        "initial_delay_seconds": 226,
        "period_seconds": 1,
        "success_threshold": 1,
        "tcp": {
            "port": 62611
        },
        "timeout_seconds": 1
    },
    startup_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 15,
        "grpc": {
            "port": 28667,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 53414,
            "scheme": "http"
        },
        "initial_delay_seconds": 1058,
        "tcp": {
            "port": 62611
        },
        "period_seconds": 3,
        "success_threshold": 2,
        "timeout_seconds": 10
    },
    queue_autoscaler={
        "desired_queue_length": 22,
        "max_replicas": 462,
        "max_downscale_per_minute": 26,
        "max_upscale_per_minute": 52,
        "min_replicas": 82,
        "polling_period": 509
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot"
)

print(result)
```

## delete_container_group

Deletes a container group

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |

**Return Type**

`ProblemDetails`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.delete_container_group(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot"
)

print(result)
```

## start_container_group

Starts a container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/start`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |

**Return Type**

`ProblemDetails`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.start_container_group(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot"
)

print(result)
```

## stop_container_group

Stops a container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/stop`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |

**Return Type**

`ProblemDetails`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot"
)

print(result)
```

## list_container_group_instances

Gets the list of container group instances

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |

**Return Type**

`ContainerGroupInstanceCollection`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot"
)

print(result)
```

## get_container_group_instance

Gets a container group instance

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}`

**Parameters**

| Name                        | Type | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name           | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | str  | ✅       | The unique container group instance identifier                                                                                                                                                                                                      |

**Return Type**

`ContainerGroupInstance`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.get_container_group_instance(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot",
    container_group_instance_id="db3a4591-efc3-46c0-b06a-3d820c0ec100"
)

print(result)
```

## update_container_group_instance

Updates a container group instance

- HTTP Method: `PATCH`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}`

**Parameters**

| Name                        | Type                                                                    | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body                | [ContainerGroupInstancePatch](../models/ContainerGroupInstancePatch.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name           | str                                                                     | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | str                                                                     | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | str                                                                     | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | str                                                                     | ✅       | The unique container group instance identifier                                                                                                                                                                                                      |

**Return Type**

`ContainerGroupInstance`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import ContainerGroupInstancePatch

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = ContainerGroupInstancePatch(
    deletion_cost=54318
)

result = sdk.container_groups.update_container_group_instance(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot",
    container_group_instance_id="db3a4591-efc3-46c0-b06a-3d820c0ec100"
)

print(result)
```

## reallocate_container_group_instance

Reallocates a container group instance to run on a different Salad Node

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/reallocate`

**Parameters**

| Name                        | Type | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name           | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | str  | ✅       | The unique container group instance identifier                                                                                                                                                                                                      |

**Return Type**

`ProblemDetails`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.reallocate_container_group_instance(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot",
    container_group_instance_id="db3a4591-efc3-46c0-b06a-3d820c0ec100"
)

print(result)
```

## recreate_container_group_instance

Stops a container, destroys it, and starts a new one without requiring the image to be downloaded again on a new Salad Node

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/recreate`

**Parameters**

| Name                        | Type | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name           | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | str  | ✅       | The unique container group instance identifier                                                                                                                                                                                                      |

**Return Type**

`ProblemDetails`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.recreate_container_group_instance(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot",
    container_group_instance_id="db3a4591-efc3-46c0-b06a-3d820c0ec100"
)

print(result)
```

## restart_container_group_instance

Stops a container and restarts it on the same Salad Node

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/restart`

**Parameters**

| Name                        | Type | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name           | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | str  | ✅       | The unique container group instance identifier                                                                                                                                                                                                      |

**Return Type**

`ProblemDetails`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot",
    container_group_instance_id="db3a4591-efc3-46c0-b06a-3d820c0ec100"
)

print(result)
```
