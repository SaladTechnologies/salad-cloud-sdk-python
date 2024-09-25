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
    name="qfojt-6ccoil4t55-ccoyybgw92dermtsdfn3t2xmag",
    display_name="O0hSlJUW",
    container={
        "image": "voluptate officia adipisicing",
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
                "host": "Ut con",
                "api_token": "nostrud irure dolore",
                "dataset": "mollit irure et Duis dolore"
            },
            "datadog": {
                "host": "pariatur",
                "api_key": "non ut",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "cupidatat cillum est sit minim",
                "ingestion_key": "dolore laboris fugiat Duis"
            },
            "splunk": {
                "host": "aliquip velit culpa",
                "token": "ex"
            },
            "tcp": {
                "host": "aliqua",
                "port": 17249
            },
            "http": {
                "host": "magna",
                "port": 62049,
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
    replicas=114,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 9813,
        "auth": False
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
    },
    queue_autoscaler={
        "min_replicas": 57,
        "max_replicas": 58,
        "desired_queue_length": 20,
        "polling_period": 1406,
        "max_upscale_per_minute": 35,
        "max_downscale_per_minute": 42
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
    organization_name="gq7z7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lw",
    project_name="xd-if9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrmz",
    container_group_name="ojjj5b9hbe2fr6f5t7j1htjaws1zx3r"
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
    display_name="-xzxtaW.t2I",
    container={
        "image": "ex cillum dolor",
        "resources": {
            "cpu": 11,
            "memory": 21424,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 12333132242
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "commodo ea exercitation pariatur consequat",
                "api_token": "ipsum",
                "dataset": "id Excepteur"
            },
            "datadog": {
                "host": "exercitation aliquip",
                "api_key": "veniam",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "amet velit sed cillum",
                "ingestion_key": "et"
            },
            "splunk": {
                "host": "proident",
                "token": "est"
            },
            "tcp": {
                "host": "ut velit ea cillum",
                "port": 13557
            },
            "http": {
                "host": "nisi fugiat cupidatat",
                "port": 60288,
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
    replicas=110,
    country_codes=[
        "af"
    ],
    networking={
        "port": 64823
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
    organization_name="gq7z7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lw",
    project_name="xd-if9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrmz",
    container_group_name="ojjj5b9hbe2fr6f5t7j1htjaws1zx3r"
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
    organization_name="gq7z7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lw",
    project_name="xd-if9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrmz",
    container_group_name="ojjj5b9hbe2fr6f5t7j1htjaws1zx3r"
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
    organization_name="zfx07sgyz1fs97sfhtue78-54vdogp2qrcnt-8a",
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
