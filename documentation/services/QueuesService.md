# QueuesService

A list of all methods in the `QueuesService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                     |
| :------------------------------------ | :---------------------------------------------- |
| [list_queues](#list_queues)           | Gets the list of queues in the given project.   |
| [create_queue](#create_queue)         | Creates a new queue in the given project.       |
| [get_queue](#get_queue)               | Gets an existing queue in the given project.    |
| [update_queue](#update_queue)         | Updates an existing queue in the given project. |
| [delete_queue](#delete_queue)         | Deletes an existing queue in the given project. |
| [list_queue_jobs](#list_queue_jobs)   | Retrieves a list of queue jobs                  |
| [create_queue_job](#create_queue_job) | Creates a new job                               |
| [get_queue_job](#get_queue_job)       | Retrieves a job in a queue                      |
| [delete_queue_job](#delete_queue_job) | Deletes a queue job                             |

## list_queues

Gets the list of queues in the given project.

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues`

**Parameters**

| Name              | Type  | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

**Return Type**

`QueueList`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queues(
    organization_name="v2321xyb8mgby4oaz0nnednrzwspo5e",
    project_name="uqcz1p0g5ye7j57a"
)

print(result)
```

## create_queue

Creates a new queue in the given project.

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues`

**Parameters**

| Name              | Type                                      | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | `[CreateQueue](../models/CreateQueue.md)` | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | `str`                                     | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str`                                     | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

**Return Type**

`Queue`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateQueue(
    name="qezkr2369ic05v6gnnllg6fhb-84kitkca0jy309-oh27ro0i5p95v4le",
    display_name="IR",
    description="consequat nulla magna minim ad"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="v2321xyb8mgby4oaz0nnednrzwspo5e",
    project_name="uqcz1p0g5ye7j57a"
)

print(result)
```

## get_queue

Gets an existing queue in the given project.

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type  | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | `str` | ✅       | The queue name.                                                                                                                                                                                                                                     |

**Return Type**

`Queue`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.get_queue(
    organization_name="ljj6uqmy01xsg7k5n8fhpr0uia1-28ec6ahk-1s6u-51xn",
    project_name="jzq0i9u27d9qsg6qsygfg",
    queue_name="d7iy1tktkoepudefqkf47dv60kqzd3q1v"
)

print(result)
```

## update_queue

Updates an existing queue in the given project.

- HTTP Method: `PATCH`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type                                      | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | `[UpdateQueue](../models/UpdateQueue.md)` | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | `str`                                     | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str`                                     | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | `str`                                     | ✅       | The queue name.                                                                                                                                                                                                                                     |

**Return Type**

`Queue`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import UpdateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateQueue(
    display_name="wfoWE",
    description="aliqua in sit"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="ljj6uqmy01xsg7k5n8fhpr0uia1-28ec6ahk-1s6u-51xn",
    project_name="jzq0i9u27d9qsg6qsygfg",
    queue_name="d7iy1tktkoepudefqkf47dv60kqzd3q1v"
)

print(result)
```

## delete_queue

Deletes an existing queue in the given project.

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type  | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | `str` | ✅       | The queue name.                                                                                                                                                                                                                                     |

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.delete_queue(
    organization_name="ljj6uqmy01xsg7k5n8fhpr0uia1-28ec6ahk-1s6u-51xn",
    project_name="jzq0i9u27d9qsg6qsygfg",
    queue_name="d7iy1tktkoepudefqkf47dv60kqzd3q1v"
)

print(result)
```

## list_queue_jobs

Retrieves a list of queue jobs

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs`

**Parameters**

| Name              | Type  | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | `str` | ✅       | The queue name.                                                                                                                                                                                                                                     |
| page              | `int` | ❌       | The page number                                                                                                                                                                                                                                     |
| page_size         | `int` | ❌       | The number of items per page                                                                                                                                                                                                                        |

**Return Type**

`QueueJobList`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="caw0rzpy61pt90mpd37q4adxw-cgodal6rzqd6z1mw1si55p9gl6eb4zgl",
    project_name="d6wezcp8h3lm398az1xa5dcxhbrhwkxlx3lw0pdkr3o5",
    queue_name="jknzh2tjfasx0nsa3dsbwz4m6an9wbi5",
    page=1762690379,
    page_size=100
)

print(result)
```

## create_queue_job

Creates a new job

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs`

**Parameters**

| Name              | Type                                            | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | `[CreateQueueJob](../models/CreateQueueJob.md)` | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | `str`                                           | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str`                                           | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | `str`                                           | ✅       | The queue name.                                                                                                                                                                                                                                     |

**Return Type**

`QueueJob`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateQueueJob

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateQueueJob(
    input="",
    metadata={},
    webhook="webhook"
)

result = sdk.queues.create_queue_job(
    request_body=request_body,
    organization_name="caw0rzpy61pt90mpd37q4adxw-cgodal6rzqd6z1mw1si55p9gl6eb4zgl",
    project_name="d6wezcp8h3lm398az1xa5dcxhbrhwkxlx3lw0pdkr3o5",
    queue_name="jknzh2tjfasx0nsa3dsbwz4m6an9wbi5"
)

print(result)
```

## get_queue_job

Retrieves a job in a queue

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs/{queue_job_id}`

**Parameters**

| Name              | Type  | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | `str` | ✅       | The queue name.                                                                                                                                                                                                                                     |
| queue_job_id      | `str` | ✅       | The job identifier. This is automatically generated and assigned when the job is created.                                                                                                                                                           |

**Return Type**

`QueueJob`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.get_queue_job(
    organization_name="qfyxrcpjzz",
    project_name="u68mnowwsycakrj2ndjibysiw6",
    queue_name="qw8v11op7e4dq1ckmwu5v289qp5d1ln00phm2",
    queue_job_id="queue_job_id"
)

print(result)
```

## delete_queue_job

Deletes a queue job

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs/{queue_job_id}`

**Parameters**

| Name              | Type  | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | `str` | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | `str` | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | `str` | ✅       | The queue name.                                                                                                                                                                                                                                     |
| queue_job_id      | `str` | ✅       | The job identifier. This is automatically generated and assigned when the job is created.                                                                                                                                                           |

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.delete_queue_job(
    organization_name="qfyxrcpjzz",
    project_name="u68mnowwsycakrj2ndjibysiw6",
    queue_name="qw8v11op7e4dq1ckmwu5v289qp5d1ln00phm2",
    queue_job_id="queue_job_id"
)

print(result)
```
