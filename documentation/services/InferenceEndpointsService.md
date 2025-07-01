# InferenceEndpointsService

A list of all methods in the `InferenceEndpointsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                           |
| :-------------------------------------------------------------- | :------------------------------------ |
| [list_inference_endpoints](#list_inference_endpoints)           | Lists inference endpoints.            |
| [get_inference_endpoint](#get_inference_endpoint)               | Gets an inference endpoint.           |
| [list_inference_endpoint_jobs](#list_inference_endpoint_jobs)   | Lists inference endpoint jobs.        |
| [create_inference_endpoint_job](#create_inference_endpoint_job) | Creates a new inference endpoint job. |
| [get_inference_endpoint_job](#get_inference_endpoint_job)       | Gets an inference endpoint job.       |
| [delete_inference_endpoint_job](#delete_inference_endpoint_job) | Cancels an inference endpoint job.    |

## list_inference_endpoints

Lists inference endpoints.

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/inference-endpoints`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| page              | int  | ❌       | The page number.                                                                                                                                                                                                                                    |
| page_size         | int  | ❌       | The maximum number of items per page.                                                                                                                                                                                                               |

**Return Type**

`InferenceEndpointCollection`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoints(
    organization_name="acme-corp",
    page=1,
    page_size=1
)

print(result)
```

## get_inference_endpoint

Gets an inference endpoint.

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}`

**Parameters**

| Name                    | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name       | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| inference_endpoint_name | str  | ✅       | The inference endpoint name.                                                                                                                                                                                                                        |

**Return Type**

`InferenceEndpoint`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint(
    organization_name="acme-corp",
    inference_endpoint_name="transcribe"
)

print(result)
```

## list_inference_endpoint_jobs

Lists inference endpoint jobs.

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs`

**Parameters**

| Name                    | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name       | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| inference_endpoint_name | str  | ✅       | The inference endpoint name.                                                                                                                                                                                                                        |
| page                    | int  | ❌       | The page number.                                                                                                                                                                                                                                    |
| page_size               | int  | ❌       | The maximum number of items per page.                                                                                                                                                                                                               |

**Return Type**

`InferenceEndpointJobCollection`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoint_jobs(
    organization_name="acme-corp",
    inference_endpoint_name="transcribe",
    page=1,
    page_size=1
)

print(result)
```

## create_inference_endpoint_job

Creates a new inference endpoint job.

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs`

**Parameters**

| Name                    | Type                                                                        | Required | Description                                                                                                                                                                                                                                         |
| :---------------------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body            | [InferenceEndpointJobPrototype](../models/InferenceEndpointJobPrototype.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name       | str                                                                         | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| inference_endpoint_name | str                                                                         | ✅       | The inference endpoint name.                                                                                                                                                                                                                        |

**Return Type**

`InferenceEndpointJob`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import InferenceEndpointJobPrototype

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = InferenceEndpointJobPrototype(
    input="",
    metadata={},
    webhook_url="https://webhook.example.com/events"
)

result = sdk.inference_endpoints.create_inference_endpoint_job(
    request_body=request_body,
    organization_name="acme-corp",
    inference_endpoint_name="transcribe"
)

print(result)
```

## get_inference_endpoint_job

Gets an inference endpoint job.

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs/{inference_endpoint_job_id}`

**Parameters**

| Name                      | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------------ | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name         | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| inference_endpoint_name   | str  | ✅       | The inference endpoint name.                                                                                                                                                                                                                        |
| inference_endpoint_job_id | str  | ✅       | The inference endpoint job identifier.                                                                                                                                                                                                              |

**Return Type**

`InferenceEndpointJob`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_job(
    organization_name="acme-corp",
    inference_endpoint_name="transcribe",
    inference_endpoint_job_id="2fc459a1-1c09-4a34-ade7-54d03fc51d6a"
)

print(result)
```

## delete_inference_endpoint_job

Cancels an inference endpoint job.

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs/{inference_endpoint_job_id}`

**Parameters**

| Name                      | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------------ | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name         | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| inference_endpoint_name   | str  | ✅       | The inference endpoint name.                                                                                                                                                                                                                        |
| inference_endpoint_job_id | str  | ✅       | The inference endpoint job identifier.                                                                                                                                                                                                              |

**Return Type**

`ProblemDetails`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.delete_inference_endpoint_job(
    organization_name="acme-corp",
    inference_endpoint_name="transcribe",
    inference_endpoint_job_id="2fc459a1-1c09-4a34-ade7-54d03fc51d6a"
)

print(result)
```
