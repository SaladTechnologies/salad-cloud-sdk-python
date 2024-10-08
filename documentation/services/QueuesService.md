# QueuesService

A list of all methods in the `QueuesService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                     |
| :------------------------------------ | :---------------------------------------------- |
| [list_queues](#list_queues)           | Gets the list of queues in the given project.   |
| [create_queue](#create_queue)         | Creates a new queue in the given project.       |
| [get_queue](#get_queue)               | Gets an existing queue in the given project.    |
| [update_queue](#update_queue)         | Updates an existing queue in the given project. |
| [delete_queue](#delete_queue)         | Deletes an existing queue in the given project. |
| [list_queue_jobs](#list_queue_jobs)   | Gets the list of jobs in a queue                |
| [create_queue_job](#create_queue_job) | Creates a new job                               |
| [get_queue_job](#get_queue_job)       | Gets a job in a queue                           |
| [delete_queue_job](#delete_queue_job) | Cancels a job in a queue                        |

## list_queues

Gets the list of queues in the given project.

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

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
    organization_name="xtp82b9jzwqov1insghigvfq0donadhrrdqx-2redu46g7e",
    project_name="xk27gbnpmwk5xor49bk4ujk7"
)

print(result)
```

## create_queue

Creates a new queue in the given project.

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues`

**Parameters**

| Name              | Type                                    | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :-------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [CreateQueue](../models/CreateQueue.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | str                                     | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str                                     | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |

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
    name="ho4d79h7bg0vpngqc8hz5pxjwi",
    display_name="IWPKHVWPTc",
    description="aliqua id nostrud"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="xtp82b9jzwqov1insghigvfq0donadhrrdqx-2redu46g7e",
    project_name="xk27gbnpmwk5xor49bk4ujk7"
)

print(result)
```

## get_queue

Gets an existing queue in the given project.

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | str  | ✅       | The queue name.                                                                                                                                                                                                                                     |

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
    organization_name="bb5wprcvb9628akhug9lnd2",
    project_name="bw-4bdb9jsi-f1xex70mdgjf5n-5ua-e28xyu9ujbls0vsy",
    queue_name="wilo12xl52y9c178cmdya6ykpby-hunb0b6s7s2l"
)

print(result)
```

## update_queue

Updates an existing queue in the given project.

- HTTP Method: `PATCH`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type                                    | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :-------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [UpdateQueue](../models/UpdateQueue.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | str                                     | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str                                     | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | str                                     | ✅       | The queue name.                                                                                                                                                                                                                                     |

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
    display_name="O5Yf2",
    description="cupidatat"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="bb5wprcvb9628akhug9lnd2",
    project_name="bw-4bdb9jsi-f1xex70mdgjf5n-5ua-e28xyu9ujbls0vsy",
    queue_name="wilo12xl52y9c178cmdya6ykpby-hunb0b6s7s2l"
)

print(result)
```

## delete_queue

Deletes an existing queue in the given project.

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | str  | ✅       | The queue name.                                                                                                                                                                                                                                     |

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
    organization_name="bb5wprcvb9628akhug9lnd2",
    project_name="bw-4bdb9jsi-f1xex70mdgjf5n-5ua-e28xyu9ujbls0vsy",
    queue_name="wilo12xl52y9c178cmdya6ykpby-hunb0b6s7s2l"
)

print(result)
```

## list_queue_jobs

Gets the list of jobs in a queue

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | str  | ✅       | The queue name.                                                                                                                                                                                                                                     |
| page              | int  | ❌       | The page number                                                                                                                                                                                                                                     |
| page_size         | int  | ❌       | The number of items per page                                                                                                                                                                                                                        |

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
    organization_name="wcaz2jbu5pfmpygxffsf4bh4e6",
    project_name="dzh9lv6afpamv8cx0x6",
    queue_name="s9f4ikmr0j6c3n18n4djttkqmgzb46dd5wogzrfe2pq12s2",
    page=706148771,
    page_size=45
)

print(result)
```

## create_queue_job

Creates a new job

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs`

**Parameters**

| Name              | Type                                          | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :-------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [CreateQueueJob](../models/CreateQueueJob.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | str                                           | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str                                           | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | str                                           | ✅       | The queue name.                                                                                                                                                                                                                                     |

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
    organization_name="wcaz2jbu5pfmpygxffsf4bh4e6",
    project_name="dzh9lv6afpamv8cx0x6",
    queue_name="s9f4ikmr0j6c3n18n4djttkqmgzb46dd5wogzrfe2pq12s2"
)

print(result)
```

## get_queue_job

Gets a job in a queue

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs/{queue_job_id}`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | str  | ✅       | The queue name.                                                                                                                                                                                                                                     |
| queue_job_id      | str  | ✅       | The job identifier. This is automatically generated and assigned when the job is created.                                                                                                                                                           |

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
    organization_name="zm-jv",
    project_name="tq26",
    queue_name="je5dpzbgsk8gvp",
    queue_job_id="queue_job_id"
)

print(result)
```

## delete_queue_job

Cancels a job in a queue

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs/{queue_job_id}`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name      | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| queue_name        | str  | ✅       | The queue name.                                                                                                                                                                                                                                     |
| queue_job_id      | str  | ✅       | The job identifier. This is automatically generated and assigned when the job is created.                                                                                                                                                           |

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
    organization_name="zm-jv",
    project_name="tq26",
    queue_name="je5dpzbgsk8gvp",
    queue_job_id="queue_job_id"
)

print(result)
```
