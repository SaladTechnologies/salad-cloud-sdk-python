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
    organization_name="gcmqvx5-larlezt8ks00ar9f8kfq524njjzfmn5dis4gk",
    project_name="x9ql9z"
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
    name="mh7g70vophyeafe4lxl6gmt4hizzzamvy3j90uelmwdmv",
    display_name="gEiIPCAh",
    description="dolor aliquip"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="gcmqvx5-larlezt8ks00ar9f8kfq524njjzfmn5dis4gk",
    project_name="x9ql9z"
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
    organization_name="s6o2b",
    project_name="z-hsy9-rgx52jml2un9bjy3nn4rykiwe0vex",
    queue_name="q77lymon4qqm4j2k111l74jgrz9lbr76iko0hba99bukkai1ci9jgia3pwf8f-v"
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
    display_name="MoX4JPAm1M.",
    description="in ea minim labore"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="s6o2b",
    project_name="z-hsy9-rgx52jml2un9bjy3nn4rykiwe0vex",
    queue_name="q77lymon4qqm4j2k111l74jgrz9lbr76iko0hba99bukkai1ci9jgia3pwf8f-v"
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
    organization_name="s6o2b",
    project_name="z-hsy9-rgx52jml2un9bjy3nn4rykiwe0vex",
    queue_name="q77lymon4qqm4j2k111l74jgrz9lbr76iko0hba99bukkai1ci9jgia3pwf8f-v"
)

print(result)
```

## list_queue_jobs

Retrieves a list of queue jobs

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
    organization_name="s3artniqzrtb3xp",
    project_name="ghu49za-gk-63eofvgj1t0umc64usbu",
    queue_name="tz9a-29ellqfizdwuu79xr4e598",
    page=1660039363,
    page_size=20
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
    organization_name="s3artniqzrtb3xp",
    project_name="ghu49za-gk-63eofvgj1t0umc64usbu",
    queue_name="tz9a-29ellqfizdwuu79xr4e598"
)

print(result)
```

## get_queue_job

Retrieves a job in a queue

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
    organization_name="q5amdp8n95tm7sbm4-h-l-za21p3dtwrf8h51jcaivs9xc",
    project_name="nhu27mdjh418v3ixyidy7jsx-nnjlyt7-bhj1c1wox",
    queue_name="tszyoxkrcz6v9wz35jltvo0g-6z9z",
    queue_job_id="queue_job_id"
)

print(result)
```

## delete_queue_job

Deletes a queue job

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
    organization_name="q5amdp8n95tm7sbm4-h-l-za21p3dtwrf8h51jcaivs9xc",
    project_name="nhu27mdjh418v3ixyidy7jsx-nnjlyt7-bhj1c1wox",
    queue_name="tszyoxkrcz6v9wz35jltvo0g-6z9z",
    queue_job_id="queue_job_id"
)

print(result)
```
