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

| Name              | Type  | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

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
    organization_name="g4zikv73wys88ns82g85qcczec2y8bnwc4gs8q6aeebojnkc8rl8-7px",
    project_name="n62j25cdo2sjh0v34w5-21z63jxnxh38ckz48-k1ecu"
)

print(result)
```

## create_container_group

Creates a new container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers`

**Parameters**

| Name              | Type                                                        | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | `[CreateContainerGroup](../models/CreateContainerGroup.md)` | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | `str`                                                       | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str`                                                       | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

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
    name="l-so4tp1yhwjdpa4rchjtb6qp-hyt0s34pmjpl-v1ax9xqfzcvrc7mg",
    display_name="655oM",
    container={
        "image": "Ut",
        "resources": {
            "cpu": 2,
            "memory": 20102,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 4874892434
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "consequat",
                "api_token": "non",
                "dataset": "tempor"
            },
            "datadog": {
                "host": "enim",
                "api_key": "aute eiusmod ad aliquip laboris",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "Excepteur Ut proident dolor",
                "ingestion_key": "aliqua amet qui"
            },
            "splunk": {
                "host": "ex id laboris laborum",
                "token": "sit"
            },
            "tcp": {
                "host": "eu sed nostrud labore",
                "port": 48807
            },
            "http": {
                "host": "elit laboris aliquip",
                "port": 45731,
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
    autostart_policy=True,
    restart_policy="always",
    replicas=3,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 26106,
        "auth": False
    },
    liveness_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
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
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 10,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
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
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 5,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
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
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 0,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    },
    queue_connection={
        "path": "ipsum proident",
        "port": 10282,
        "queue_name": "cnb3eo62nsjao0"
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="g4zikv73wys88ns82g85qcczec2y8bnwc4gs8q6aeebojnkc8rl8-7px",
    project_name="n62j25cdo2sjh0v34w5-21z63jxnxh38ckz48-k1ecu"
)

print(result)
```

## get_container_group

Gets a container group

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type  | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |

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
    organization_name="xpjrui87jps52s0iy",
    project_name="hd-g9wqh8bjget2tyh4q9ni9h81tilnlnf5i-r38a8vv5h4lnt5rb91fzs2",
    container_group_name="naw4grzs1ulr8elj96ymws1tye0"
)

print(result)
```

## update_container_group

Updates a container group

- HTTP Method: `PATCH`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type                                                        | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | `[UpdateContainerGroup](../models/UpdateContainerGroup.md)` | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name    | `str`                                                       | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | `str`                                                       | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | `str`                                                       | ✅       | The unique container group name                                                                                                                                                                                                                     |

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
    display_name="v9k",
    container={
        "image": "mollit exercitation",
        "resources": {
            "cpu": 11,
            "memory": 17397,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 53243271378
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "Lorem esse minim enim",
                "api_token": "eiusmod",
                "dataset": "incididunt ut Ut"
            },
            "datadog": {
                "host": "Excepteur",
                "api_key": "sit nisi nulla esse",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "anim",
                "ingestion_key": "id velit Lorem"
            },
            "splunk": {
                "host": "sint nostrud sunt anim commodo",
                "token": "eu culpa voluptate ut"
            },
            "tcp": {
                "host": "do eu Ut minim mollit",
                "port": 51879
            },
            "http": {
                "host": "in sit Excepteur dolor consectetur",
                "port": 16123,
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
    replicas=57,
    country_codes=[
        "af"
    ],
    networking={
        "port": 27521
    },
    liveness_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
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
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 10,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
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
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 5,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
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
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 0,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="xpjrui87jps52s0iy",
    project_name="hd-g9wqh8bjget2tyh4q9ni9h81tilnlnf5i-r38a8vv5h4lnt5rb91fzs2",
    container_group_name="naw4grzs1ulr8elj96ymws1tye0"
)

print(result)
```

## delete_container_group

Deletes a container group

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type  | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |

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
    organization_name="xpjrui87jps52s0iy",
    project_name="hd-g9wqh8bjget2tyh4q9ni9h81tilnlnf5i-r38a8vv5h4lnt5rb91fzs2",
    container_group_name="naw4grzs1ulr8elj96ymws1tye0"
)

print(result)
```

## start_container_group

Starts a container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/start`

**Parameters**

| Name                 | Type  | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |

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
    organization_name="qv-nsi3p0ihren7kh3cozmla70bry",
    project_name="nwspw00apvowm2uk3ia7vi9jlaex78t719gjcf-7ed",
    container_group_name="jmguhpzfluex6-1ksn8mw9"
)

print(result)
```

## stop_container_group

Stops a container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/stop`

**Parameters**

| Name                 | Type  | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |

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
    organization_name="akn0y-5uryou3umpp3jva-wgcda23a08440n-ew1-q",
    project_name="im",
    container_group_name="d9iq2qrkhhpqc1ii57w5xgt26suu70u1qechp"
)

print(result)
```

## list_container_group_instances

Retrieves a list of container group instances

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances`

**Parameters**

| Name                 | Type  | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |

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
    organization_name="x9apf4t0-uai3sdl150pq-zx5u-9-j",
    project_name="bz4mp1vscg2wjxeuemfxcv-ue7tm-bp-8n1hvh8fnv7mx285iuup332rpaf",
    container_group_name="shaiuchf2q8kkg3dsgwkty0ap7uq2b1ex4akekgljza8i9375vs22d352n"
)

print(result)
```

## get_container_group_instance

Retrieves the details of a single instance within a container group by instance ID

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}`

**Parameters**

| Name                        | Type  | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name           | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | `str` | ✅       | The unique instance identifier                                                                                                                                                                                                                      |

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
    organization_name="bsf7v",
    project_name="ulau11f5g2zdmdpxhrfzhv7x3dhck87lv8-z-v",
    container_group_name="efzk8ea2roe6yryt0-t1885dp762ut0igkfak4jbmum3tb50ov",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## reallocate_container_group_instance

Remove a node from a workload and reallocate the workload to a different node

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/reallocate`

**Parameters**

| Name                        | Type  | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name           | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | `str` | ✅       | The unique instance identifier                                                                                                                                                                                                                      |

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
    organization_name="cq7z43vbdm-ym2fjvtwvm3kubeomi0c157pyuvzjd-oj09gh",
    project_name="rxoh7290af1yiwyo8xtgc4vo",
    container_group_name="wsr245-lzbbnxajonfxep9ngo2h6p4ol",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## recreate_container_group_instance

Stops a container, destroys it, creates a new one without requiring the image to be downloaded again on a different node

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/recreate`

**Parameters**

| Name                        | Type  | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name           | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | `str` | ✅       | The unique instance identifier                                                                                                                                                                                                                      |

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
    organization_name="dqryzs0nwtgem9",
    project_name="s1kzoxeehf59gi91ttsn9ueh4r0udym74yor3eg40ckc",
    container_group_name="r227v3cr3",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## restart_container_group_instance

Restarts a workload on a node without reallocating it

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/restart`

**Parameters**

| Name                        | Type  | Required | Description                                                                                                                                                                                                                                         |
| :-------------------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name           | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name                | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name        | `str` | ✅       | The unique container group name                                                                                                                                                                                                                     |
| container_group_instance_id | `str` | ✅       | The unique instance identifier                                                                                                                                                                                                                      |

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
    organization_name="x2hb606akllhe-z9w578p05ni",
    project_name="czv80xtiift-dhcux3behoqegicbjgytvavm7ngiki6uxl76eoewg5dgz5g",
    container_group_name="f3mzshp",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```
