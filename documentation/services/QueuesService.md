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
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.list_queues(
    organization_name="j-8a4o7jhy3jn2rdf012fi7ouno3mk-ax3",
    project_name="cajj5ajjquzeg-z3kvqxtnoxnlzhjhjt-8nawc40o0gqev9"
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
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateQueue(
    name="name",
    display_name=" 6zTtRPsvOk",
    description="description"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="j-8a4o7jhy3jn2rdf012fi7ouno3mk-ax3",
    project_name="cajj5ajjquzeg-z3kvqxtnoxnlzhjhjt-8nawc40o0gqev9"
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
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.get_queue(
    organization_name="inu8izbgz",
    project_name="ynu6-fkv4dta4ydy-pi16e4ddle58fi8u9w2qgnsg",
    queue_name="gcnci4p90a72aagy0f001ws1rwna83a3asu0izd6ugn07m5xpcp89lefe"
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
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import UpdateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = UpdateQueue(
    display_name="2E4g",
    description="description"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="inu8izbgz",
    project_name="ynu6-fkv4dta4ydy-pi16e4ddle58fi8u9w2qgnsg",
    queue_name="gcnci4p90a72aagy0f001ws1rwna83a3asu0izd6ugn07m5xpcp89lefe"
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
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.delete_queue(
    organization_name="inu8izbgz",
    project_name="ynu6-fkv4dta4ydy-pi16e4ddle58fi8u9w2qgnsg",
    queue_name="gcnci4p90a72aagy0f001ws1rwna83a3asu0izd6ugn07m5xpcp89lefe"
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
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="w4s9eg1d2caksvlhpzmfccbh2v7dcapp3enb9gd2f4k4",
    project_name="yviu53s67ckwwnxsd-gfjsmuxcljdg4t1zzyn",
    queue_name="gpl2kuh4c67m3ae7qwlwipkdye-ad90-cq0up7kyr7vabeivb96iw",
    page=124963738,
    page_size=59
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
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateQueueJob

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateQueueJob(
    input="",
    metadata={},
    webhook="webhook"
)

result = sdk.queues.create_queue_job(
    request_body=request_body,
    organization_name="w4s9eg1d2caksvlhpzmfccbh2v7dcapp3enb9gd2f4k4",
    project_name="yviu53s67ckwwnxsd-gfjsmuxcljdg4t1zzyn",
    queue_name="gpl2kuh4c67m3ae7qwlwipkdye-ad90-cq0up7kyr7vabeivb96iw"
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
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.get_queue_job(
    organization_name="hvm1ntcgljb71tp82b9jzwqov1insghigvfq0d",
    project_name="kadhrrdqx-2redu46g7e7nk1",
    queue_name="xbnpmwk5xor3",
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
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.delete_queue_job(
    organization_name="hvm1ntcgljb71tp82b9jzwqov1insghigvfq0d",
    project_name="kadhrrdqx-2redu46g7e7nk1",
    queue_name="xbnpmwk5xor3",
    queue_job_id="queue_job_id"
)

print(result)
```
