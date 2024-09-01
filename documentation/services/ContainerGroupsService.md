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

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |
| project_name      | str  | ✅       | The unique project name      |

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
    organization_name="apihl1d8o144-mf49qtwmztxy5e3c9v5qfb4l0g8j1lcj9-nh4i6dz2e7jf3",
    project_name="vjbveijqip5mysgje2g39crv0td0zupa8uxmseld79zsgkh7je6z"
)

print(result)
```

## create_container_group

Creates a new container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers`

**Parameters**

| Name              | Type                                                      | Required | Description                  |
| :---------------- | :-------------------------------------------------------- | :------- | :--------------------------- |
| request_body      | [CreateContainerGroup](../models/CreateContainerGroup.md) | ✅       | The request body.            |
| organization_name | str                                                       | ✅       | The unique organization name |
| project_name      | str                                                       | ✅       | The unique project name      |

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
    name="qqgh5gtdxccg-tsuo",
    display_name="0GALm",
    container={
        "image": "exercitation eu pariatur elit adipisicing",
        "resources": {
            "cpu": 12,
            "memory": 26125,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 30852754821
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "incididunt cupidatat",
                "api_token": "ullamco",
                "dataset": "ad nisi laborum"
            },
            "datadog": {
                "host": "sint",
                "api_key": "labore cupidatat",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "cupidatat",
                "ingestion_key": "dolor occaecat in dolore in"
            },
            "splunk": {
                "host": "cillum in dolor",
                "token": "ex incididunt elit adipisicing"
            },
            "tcp": {
                "host": "incididunt fugiat enim officia sed",
                "port": 30285
            },
            "http": {
                "host": "enim magna esse",
                "port": 30824,
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
    replicas=81,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 4886,
        "auth": False
    },
    liveness_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 0,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 9,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
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
        "path": "velit elit",
        "port": 7009,
        "queue_name": "wh1ewe-69ifjpdhw0h4i3hwpdzw-n1fpjd0naycxeb1u1iiyrp-4y1t7"
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="apihl1d8o144-mf49qtwmztxy5e3c9v5qfb4l0g8j1lcj9-nh4i6dz2e7jf3",
    project_name="vjbveijqip5mysgje2g39crv0td0zupa8uxmseld79zsgkh7je6z"
)

print(result)
```

## get_container_group

Gets a container group

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type | Required | Description                     |
| :------------------- | :--- | :------- | :------------------------------ |
| organization_name    | str  | ✅       | The unique organization name    |
| project_name         | str  | ✅       | The unique project name         |
| container_group_name | str  | ✅       | The unique container group name |

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
    organization_name="a147vxii7gy6-eg0n389rp",
    project_name="zcgtz8t87b",
    container_group_name="jonf9u1s785z-11dylxjw4966ge-9p6qcjc-qtefzoj09ev3nsih"
)

print(result)
```

## update_container_group

Updates a container group

- HTTP Method: `PATCH`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type                                                      | Required | Description                     |
| :------------------- | :-------------------------------------------------------- | :------- | :------------------------------ |
| request_body         | [UpdateContainerGroup](../models/UpdateContainerGroup.md) | ✅       | The request body.               |
| organization_name    | str                                                       | ✅       | The unique organization name    |
| project_name         | str                                                       | ✅       | The unique project name         |
| container_group_name | str                                                       | ✅       | The unique container group name |

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
    display_name="s1RiI 0-",
    container={
        "image": "ipsum pariatur non proident dolore",
        "resources": {
            "cpu": 2,
            "memory": 19703,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 4820479057
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "aliquip magna est ex tempor",
                "api_token": "esse magna eu ut amet",
                "dataset": "in pariatur Duis non"
            },
            "datadog": {
                "host": "Duis",
                "api_key": "id magna cupidatat ipsum aliqua",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "Duis culpa cillum",
                "ingestion_key": "exercitation sint aute aliqua ex"
            },
            "splunk": {
                "host": "ex culpa exercitation ad proident",
                "token": "laborum"
            },
            "tcp": {
                "host": "pariatur",
                "port": 45370
            },
            "http": {
                "host": "ut in et quis adipisicing",
                "port": 33069,
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
    replicas=97,
    country_codes=[
        "af"
    ],
    networking={
        "port": 14234
    },
    liveness_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 0,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 9,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
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
    organization_name="a147vxii7gy6-eg0n389rp",
    project_name="zcgtz8t87b",
    container_group_name="jonf9u1s785z-11dylxjw4966ge-9p6qcjc-qtefzoj09ev3nsih"
)

print(result)
```

## delete_container_group

Deletes a container group

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}`

**Parameters**

| Name                 | Type | Required | Description                     |
| :------------------- | :--- | :------- | :------------------------------ |
| organization_name    | str  | ✅       | The unique organization name    |
| project_name         | str  | ✅       | The unique project name         |
| container_group_name | str  | ✅       | The unique container group name |

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
    organization_name="a147vxii7gy6-eg0n389rp",
    project_name="zcgtz8t87b",
    container_group_name="jonf9u1s785z-11dylxjw4966ge-9p6qcjc-qtefzoj09ev3nsih"
)

print(result)
```

## start_container_group

Starts a container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/start`

**Parameters**

| Name                 | Type | Required | Description                     |
| :------------------- | :--- | :------- | :------------------------------ |
| organization_name    | str  | ✅       | The unique organization name    |
| project_name         | str  | ✅       | The unique project name         |
| container_group_name | str  | ✅       | The unique container group name |

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
    organization_name="jsq6na2w8d2wlvk-85d3jxhjhjigc",
    project_name="fv6oyiqlky7x2i-whfkhuex4ceacw4n3kgc3y89xb",
    container_group_name="a17zo0pyz6xi8-xbb6y7-prw04kcruh1moxld03jx91-zpoej07l0146fz"
)

print(result)
```

## stop_container_group

Stops a container group

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/stop`

**Parameters**

| Name                 | Type | Required | Description                     |
| :------------------- | :--- | :------- | :------------------------------ |
| organization_name    | str  | ✅       | The unique organization name    |
| project_name         | str  | ✅       | The unique project name         |
| container_group_name | str  | ✅       | The unique container group name |

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
    organization_name="ohrlrstei115qknuq5qe4nwnj",
    project_name="mb04z87rwlzn3oww-l1t2vxu9r52mu126bs1owp2gdjes6jc5ch-ei3t5i",
    container_group_name="kda80pcf6aqiptmp19a40ofjecyop-nmf2k9mz2fveuxwp-0fo3gm2pxa"
)

print(result)
```

## list_container_group_instances

Retrieves a list of container group instances

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances`

**Parameters**

| Name                 | Type | Required | Description                     |
| :------------------- | :--- | :------- | :------------------------------ |
| organization_name    | str  | ✅       | The unique organization name    |
| project_name         | str  | ✅       | The unique project name         |
| container_group_name | str  | ✅       | The unique container group name |

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
    organization_name="i4i4ci3lnqp4d8my25qe5eucwfr0ni9ksw1jelhxjh",
    project_name="jfbvsusu0d8a1e8x94q0wsip8olrhfnnvkr7bgvgo196fb90srivpmzldjm59q",
    container_group_name="jk7y5mmm88"
)

print(result)
```

## get_container_group_instance

Retrieves the details of a single instance within a container group by instance ID

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}`

**Parameters**

| Name                        | Type | Required | Description                     |
| :-------------------------- | :--- | :------- | :------------------------------ |
| organization_name           | str  | ✅       | The unique organization name    |
| project_name                | str  | ✅       | The unique project name         |
| container_group_name        | str  | ✅       | The unique container group name |
| container_group_instance_id | str  | ✅       | The unique instance identifier  |

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
    organization_name="r3b4l8zryeh7q3m-b8y1cgkv",
    project_name="lw3mzmlm01jbt-edmy-frcr",
    container_group_name="jahux-5",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## reallocate_container_group_instance

Remove a node from a workload and reallocate the workload to a different node

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/reallocate`

**Parameters**

| Name                        | Type | Required | Description                     |
| :-------------------------- | :--- | :------- | :------------------------------ |
| organization_name           | str  | ✅       | The unique organization name    |
| project_name                | str  | ✅       | The unique project name         |
| container_group_name        | str  | ✅       | The unique container group name |
| container_group_instance_id | str  | ✅       | The unique instance identifier  |

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
    organization_name="bmy1l0br-rmixwbvc9ty97juj635ydst",
    project_name="q3p4vyxuezsi2df5k3zo",
    container_group_name="k8xkphecgevqm3hvsc67whgqy-mn014uo7xy84n57s-p1hdusj8g4tnc0b",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## recreate_container_group_instance

Stops a container, destroys it, creates a new one without requiring the image to be downloaded again on a different node

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/recreate`

**Parameters**

| Name                        | Type | Required | Description                     |
| :-------------------------- | :--- | :------- | :------------------------------ |
| organization_name           | str  | ✅       | The unique organization name    |
| project_name                | str  | ✅       | The unique project name         |
| container_group_name        | str  | ✅       | The unique container group name |
| container_group_instance_id | str  | ✅       | The unique instance identifier  |

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
    organization_name="qz-vxewuk2trppo3qsv4l21p7b-ff5slo4yczyvujato6654uo",
    project_name="u7gkyhv80k2lnlplemq9834io55hrceikk4fyg6zd3i-m174lzoyodgcj9f1f",
    container_group_name="ngdah36m21h5",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```

## restart_container_group_instance

Restarts a workload on a node without reallocating it

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/instances/{container_group_instance_id}/restart`

**Parameters**

| Name                        | Type | Required | Description                     |
| :-------------------------- | :--- | :------- | :------------------------------ |
| organization_name           | str  | ✅       | The unique organization name    |
| project_name                | str  | ✅       | The unique project name         |
| container_group_name        | str  | ✅       | The unique container group name |
| container_group_instance_id | str  | ✅       | The unique instance identifier  |

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
    organization_name="q4bvcc9w5lcg",
    project_name="ar4nzwg42bty8xw-dowooq-ycquvtr7pp0h2y24hkt0ps",
    container_group_name="j0s47o7jvc3kavg47t-viw2vz0xrxk6qarbrczxkh6",
    container_group_instance_id="container_group_instance_id"
)

print(result)
```
