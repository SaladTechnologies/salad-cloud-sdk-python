# QueuesService

A list of all methods in the `QueuesService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                    |
| :------------------------------------ | :----------------------------- |
| [list_queues](#list_queues)           | Gets the list of queues        |
| [create_queue](#create_queue)         | Creates a new queue            |
| [get_queue](#get_queue)               | Gets a queue                   |
| [update_queue](#update_queue)         | Updates a queue                |
| [delete_queue](#delete_queue)         | Deletes a queue                |
| [list_queue_jobs](#list_queue_jobs)   | Retrieves a list of queue jobs |
| [create_queue_job](#create_queue_job) | Creates a new job              |
| [get_queue_job](#get_queue_job)       | Retrieves a job in a queue     |
| [delete_queue_job](#delete_queue_job) | Deletes a queue job            |

## list_queues

Gets the list of queues

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |
| project_name      | str  | ✅       | The unique project name      |

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
    organization_name="tuw6h14q4yanz6jzs-93quj",
    project_name="zd-1kwc3qrr2qrta5-ma5yft7izvjtyvbpfqpzas8ys0rleuecgeq"
)

print(result)
```

## create_queue

Creates a new queue

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues`

**Parameters**

| Name              | Type                                    | Required | Description                  |
| :---------------- | :-------------------------------------- | :------- | :--------------------------- |
| request_body      | [CreateQueue](../models/CreateQueue.md) | ✅       | The request body.            |
| organization_name | str                                     | ✅       | The unique organization name |
| project_name      | str                                     | ✅       | The unique project name      |

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
    name="ctrq4osv0lra1vqw6",
    display_name="snv",
    description="irure commodo ipsum veniam tempor"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="tuw6h14q4yanz6jzs-93quj",
    project_name="zd-1kwc3qrr2qrta5-ma5yft7izvjtyvbpfqpzas8ys0rleuecgeq"
)

print(result)
```

## get_queue

Gets a queue

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |
| project_name      | str  | ✅       | The unique project name      |
| queue_name        | str  | ✅       | The unique queue name        |

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
    organization_name="j0404lk6i34cuer",
    project_name="ekiabi4sbb23l56oq87j1v",
    queue_name="w4hdchyg-8n5glaql3-539c26ytntnk7-le269faihpgelqal6jc72"
)

print(result)
```

## update_queue

Updates a queue

- HTTP Method: `PATCH`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type                                    | Required | Description                  |
| :---------------- | :-------------------------------------- | :------- | :--------------------------- |
| request_body      | [UpdateQueue](../models/UpdateQueue.md) | ✅       | The request body.            |
| organization_name | str                                     | ✅       | The unique organization name |
| project_name      | str                                     | ✅       | The unique project name      |
| queue_name        | str                                     | ✅       | The unique queue name        |

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
    display_name="tgkuNWMcC",
    description="in"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="j0404lk6i34cuer",
    project_name="ekiabi4sbb23l56oq87j1v",
    queue_name="w4hdchyg-8n5glaql3-539c26ytntnk7-le269faihpgelqal6jc72"
)

print(result)
```

## delete_queue

Deletes a queue

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |
| project_name      | str  | ✅       | The unique project name      |
| queue_name        | str  | ✅       | The unique queue name        |

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
    organization_name="j0404lk6i34cuer",
    project_name="ekiabi4sbb23l56oq87j1v",
    queue_name="w4hdchyg-8n5glaql3-539c26ytntnk7-le269faihpgelqal6jc72"
)

print(result)
```

## list_queue_jobs

Retrieves a list of queue jobs

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |
| project_name      | str  | ✅       | The unique project name      |
| queue_name        | str  | ✅       | The unique queue name        |
| page              | int  | ❌       | The page number              |
| page_size         | int  | ❌       | The number of items per page |

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
    organization_name="iugscfp5-4x1xl1-c1ax256",
    project_name="noy7vldsml0wxbxw",
    queue_name="sdtl98ziqb",
    page=477149090,
    page_size=12
)

print(result)
```

## create_queue_job

Creates a new job

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs`

**Parameters**

| Name              | Type                                          | Required | Description                  |
| :---------------- | :-------------------------------------------- | :------- | :--------------------------- |
| request_body      | [CreateQueueJob](../models/CreateQueueJob.md) | ✅       | The request body.            |
| organization_name | str                                           | ✅       | The unique organization name |
| project_name      | str                                           | ✅       | The unique project name      |
| queue_name        | str                                           | ✅       | The unique queue name        |

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
    organization_name="iugscfp5-4x1xl1-c1ax256",
    project_name="noy7vldsml0wxbxw",
    queue_name="sdtl98ziqb"
)

print(result)
```

## get_queue_job

Retrieves a job in a queue

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs/{queue_job_id}`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |
| project_name      | str  | ✅       | The unique project name      |
| queue_name        | str  | ✅       | The unique queue name        |
| queue_job_id      | str  | ✅       | The unique job id            |

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
    organization_name="vxqcbddvaoe06qhpuoplm89wi2894q9cpfigd95ewlngasgx2e93zxei",
    project_name="iri0-iro9w0j3jvvgj2awj6-0ivo86",
    queue_name="e7zccce0i4ccb53k4gtsp-47yvqix8go1831z2sf2i8",
    queue_job_id="queue_job_id"
)

print(result)
```

## delete_queue_job

Deletes a queue job

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/queues/{queue_name}/jobs/{queue_job_id}`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |
| project_name      | str  | ✅       | The unique project name      |
| queue_name        | str  | ✅       | The unique queue name        |
| queue_job_id      | str  | ✅       | The unique job id            |

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
    organization_name="vxqcbddvaoe06qhpuoplm89wi2894q9cpfigd95ewlngasgx2e93zxei",
    project_name="iri0-iro9w0j3jvvgj2awj6-0ivo86",
    queue_name="e7zccce0i4ccb53k4gtsp-47yvqix8go1831z2sf2i8",
    queue_job_id="queue_job_id"
)

print(result)
```
