# ContainerGroupsService

A list of all methods in the `ContainerGroupsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                              |
| :-------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| [list_container_groups](#list_container_groups)                             | Gets the list of container groups                                                                                        |
| [create_container_group](#create_container_group)                           | Creates a new container group                                                                                            |
| [get_container_group](#get_container_group)                                 | Gets a container group                                                                                                   |
| [update_container_group](#update_container_group)                           | Updates a container group                                                                                                |
| [delete_container_group](#delete_container_group)                           | Deletes a container group                                                                                                |
| [start_container_group](#start_container_group)                             | Starts a container group                                                                                                 |
| [stop_container_group](#stop_container_group)                               | Stops a container group                                                                                                  |
| [list_container_group_instances](#list_container_group_instances)           | Retrieves a list of container group instances                                                                            |
| [get_container_group_instance](#get_container_group_instance)               | Retrieves the details of a single instance within a container group by instance ID                                       |
| [reallocate_container_group_instance](#reallocate_container_group_instance) | Remove a node from a workload and reallocate the workload to a different node                                            |
| [recreate_container_group_instance](#recreate_container_group_instance)     | Stops a container, destroys it, creates a new one without requiring the image to be downloaded again on a different node |
| [restart_container_group_instance](#restart_container_group_instance)       | Restarts a workload on a node without reallocating it                                                                    |

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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_groups(
    organization_name="v50imwzgi4em4q035",
    project_name="m6yw3-xm60cb7tiev8rketqiiwjepibzf2ust1cvjx8oua8mepeueo5-1"
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
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateContainerGroup

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateContainerGroup(
    name="oh2mpxyfojt-6cco",
    display_name="HoT",
    container={
        "image": "velit qui cillum veniam ullamco",
        "resources": {
            "cpu": 10,
            "memory": 17858,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 32391110488
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "in culpa aute",
                "api_token": "mollit culpa",
                "dataset": "qui nulla laborum ex"
            },
            "datadog": {
                "host": "id fugiat cillum",
                "api_key": "nostrud",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "en",
                "ingestion_key": "aliqua ad laboris anim"
            },
            "splunk": {
                "host": "enim cupidatat eiusmod",
                "token": "do"
            },
            "tcp": {
                "host": "aliquip labore dolor id",
                "port": 45778
            },
            "http": {
                "host": "pariatur",
                "port": 16204,
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
        }
    },
    autostart_policy=False,
    restart_policy="always",
    replicas=225,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 19760,
        "auth": True
    },
    liveness_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 5,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
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
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 4,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    },
    queue_connection={
        "path": "ullamco magna est nulla aliqua",
        "port": 49952,
        "queue_name": "nnz26lyemw7nednorlqjlsihb42092pn8d"
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="v50imwzgi4em4q035",
    project_name="m6yw3-xm60cb7tiev8rketqiiwjepibzf2ust1cvjx8oua8mepeueo5-1"
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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group(
    organization_name="ob3ca5hduqlb1uzytbhhukf1u0-ahl0b9oqfjj0q",
    project_name="x7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lx71",
    container_group_name="cif9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrm0urjjj5b9hbe2fr6f"
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
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import UpdateContainerGroup

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateContainerGroup(
    display_name="UtDi9VD ZS",
    container={
        "image": "culpa nulla eu non",
        "resources": {
            "cpu": 11,
            "memory": 1557,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 40250176413
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "nisi et veniam",
                "api_token": "Lorem esse dolor",
                "dataset": "et commodo Duis"
            },
            "datadog": {
                "host": "veniam deserunt sunt dolore",
                "api_key": "ullamco occaecat nostrud irure",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "dolor adipisicing eu dolore incididunt",
                "ingestion_key": "aliqua"
            },
            "splunk": {
                "host": "enim incididunt",
                "token": "Lorem Duis ipsum et"
            },
            "tcp": {
                "host": "qui in cupidatat deserunt cillum",
                "port": 39897
            },
            "http": {
                "host": "nostrud ea dolore",
                "port": 52587,
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
        }
    },
    replicas=183,
    country_codes=[
        "af"
    ],
    networking={
        "port": 60033
    },
    liveness_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 5,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
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
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 4,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="ob3ca5hduqlb1uzytbhhukf1u0-ahl0b9oqfjj0q",
    project_name="x7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lx71",
    container_group_name="cif9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrm0urjjj5b9hbe2fr6f"
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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.delete_container_group(
    organization_name="ob3ca5hduqlb1uzytbhhukf1u0-ahl0b9oqfjj0q",
    project_name="x7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lx71",
    container_group_name="cif9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrm0urjjj5b9hbe2fr6f"
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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.start_container_group(
    organization_name="uh5upyur493wxwbxrj4xt9wfx07sgyz1fs97sfhtue78-54vdogp2qrcnt-8a",
    project_name="v7jhy3jn2rdf012fi7ouno3mk9",
    container_group_name="a4d0ajj5ajjquzeg-z3kvqxtnoxnlzhjhjt-8naw"
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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="c0o0gqev-mnkpy8af-s7rq68p2lenu8izbg09xnu6-fkv4dta4yd",
    project_name="rpi16e4ddle58fi8u9w2qgnsgj7cnci4p90a72aagy0f001ws1rwna83a3asuz",
    container_group_name="fd6ugn07m5xpcp89lefemdke05z4s9eg1d2caksvlhpzm"
)

print(result)
```

## list_container_group_instances

Retrieves a list of container group instances

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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="dcbh1",
    project_name="pdcapp3enb9gd2f4k49vviu53s67ckwwnxsd-gfjsmuxcljdg4t1zzyoj",
    container_group_name="vl2kuh4c67m3ae7qwlwipkdye-ad"
)

print(result)
```

## get_container_group_instance

Retrieves the details of a single instance within a container group by instance ID

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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group_instance(
    organization_name="b0up7kyr7vabeivb96iwcvlvvm1n",
    project_name="ngljb",
    container_group_name="xtp82b9jzwqov1insghigvfq0donadhrrdqx-2redu46g7e",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## reallocate_container_group_instance

Remove a node from a workload and reallocate the workload to a different node

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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.reallocate_container_group_instance(
    organization_name="xk27gbnpmwk5xor49bk4ujk7",
    project_name="cy1l6xj-5vzihwp4ho850l3faynnuq71ru6y",
    container_group_name="mgza-e8llajq25o36x8b-38phh",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## recreate_container_group_instance

Stops a container, destroys it, creates a new one without requiring the image to be downloaded again on a different node

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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.recreate_container_group_instance(
    organization_name="pkfh3rhnvt4x30k5t",
    project_name="o7r3q30xz",
    container_group_name="aq7hd1fjfxgtq8uehil3eplo",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## restart_container_group_instance

Restarts a workload on a node without reallocating it

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
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="kd79h7bg0vpngqc8hz5pxjwi7muqnmuuqsx3q3zm2hxkci5yv6kho",
    project_name="u5ljgqmbs6a7s",
    container_group_name="qmq3nj6oy8b2wpzbidnelidy9s6k9w",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```
