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

`ContainerGroupList`

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

| Name              | Type                                                      | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [CreateContainerGroup](../models/CreateContainerGroup.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | str                                                       | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str                                                       | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

**Return Type**

`ContainerGroup`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateContainerGroup

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateContainerGroup(
    name="name",
    display_name="uPpL",
    container={
        "image": "image",
        "resources": {
            "cpu": 7,
            "memory": 51618,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 23627499788
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
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
                "port": 14084
            },
            "http": {
                "host": "host",
                "port": 31838,
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
            }
        },
        "registry_authentication": {
            "basic": {
                "username": "username",
                "password": "password"
            },
            "gcp_gcr": {
                "service_key": "service_key"
            },
            "aws_ecr": {
                "access_key_id": "access_key_id",
                "secret_access_key": "secret_access_key"
            },
            "docker_hub": {
                "username": "username",
                "personal_access_token": "personal_access_token"
            },
            "gcp_gar": {
                "service_key": "service_key"
            }
        },
        "image_caching": False
    },
    autostart_policy=False,
    restart_policy="always",
    replicas=437,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 51618,
        "auth": True,
        "load_balancer": "round_robin",
        "single_connection_limit": True,
        "client_request_timeout": 100000,
        "server_response_timeout": 100000
    },
    liveness_probe={
        "tcp": {
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 43451
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 2,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 43451
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 6,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 43451
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 7,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    },
    queue_connection={
        "path": "path",
        "port": 33046,
        "queue_name": "dbfand1htyt3qna2yfhck403bsaqbf"
    },
    queue_autoscaler={
        "min_replicas": 60,
        "max_replicas": 62,
        "desired_queue_length": 67,
        "polling_period": 39,
        "max_upscale_per_minute": 62,
        "max_downscale_per_minute": 52
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
    container_group_name="vpg4-370h--6se6eqezp-g"
)

print(result)
```

## update_container_group

Updates a container group

- HTTP Method: `PATCH`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type                                                      | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [UpdateContainerGroup](../models/UpdateContainerGroup.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name    | str                                                       | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str                                                       | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str                                                       | ✅       | The unique container group name                                                                                                                                                                                                                     |

**Return Type**

`ContainerGroup`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import UpdateContainerGroup

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = UpdateContainerGroup(
    display_name="iMQ",
    container={
        "image": "image",
        "resources": {
            "cpu": 1,
            "memory": 45763,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 11277160494
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
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
                "port": 30411
            },
            "http": {
                "host": "host",
                "port": 32913,
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
            }
        },
        "registry_authentication": {
            "basic": {
                "username": "username",
                "password": "password"
            },
            "gcp_gcr": {
                "service_key": "service_key"
            },
            "aws_ecr": {
                "access_key_id": "access_key_id",
                "secret_access_key": "secret_access_key"
            },
            "docker_hub": {
                "username": "username",
                "personal_access_token": "personal_access_token"
            },
            "gcp_gar": {
                "service_key": "service_key"
            }
        },
        "image_caching": False
    },
    replicas=201,
    country_codes=[
        "af"
    ],
    networking={
        "port": 16494
    },
    liveness_probe={
        "tcp": {
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 43451
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 2,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 43451
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 6,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 43451
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 7,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    },
    queue_autoscaler={
        "min_replicas": 60,
        "max_replicas": 62,
        "desired_queue_length": 67,
        "polling_period": 39,
        "max_upscale_per_minute": 62,
        "max_downscale_per_minute": 52
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="vpg4-370h--6se6eqezp-g"
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
    container_group_name="vpg4-370h--6se6eqezp-g"
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
    container_group_name="brlw5vvch4r0"
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
    container_group_name="jkyg"
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

`ContainerGroupInstances`

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
    container_group_name="gd6c-o-5jwj2ocq-dvadg2cp1l-tkh9w1m"
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
| container_group_instance_id | str  | ✅       | The unique instance identifier                                                                                                                                                                                                                      |

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
    container_group_name="o-9nad5ncpxu9ccs7p0whu98gpr-2299jnynn9io8wrozbk",
    container_group_instance_id="container_group_instance_id"
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
| container_group_instance_id | str  | ✅       | The unique instance identifier                                                                                                                                                                                                                      |

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
    container_group_name="dc9etpxe",
    container_group_instance_id="container_group_instance_id"
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
| container_group_instance_id | str  | ✅       | The unique instance identifier                                                                                                                                                                                                                      |

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
    container_group_name="k8avj5fo61fav",
    container_group_instance_id="container_group_instance_id"
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
| container_group_instance_id | str  | ✅       | The unique instance identifier                                                                                                                                                                                                                      |

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
    container_group_name="zq13ml41ozl1iikkkwnv9cb7ost0zdsg3j-k54cvkw1mdc165omi3xku5rq32",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```
