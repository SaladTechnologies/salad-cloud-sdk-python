# InferenceEndpointsService

A list of all methods in the `InferenceEndpointsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                    |
| :-------------------------------------------------------------- | :--------------------------------------------- |
| [list_inference_endpoints](#list_inference_endpoints)           | Gets the list of all inference endpoints       |
| [get_inference_endpoint](#get_inference_endpoint)               | Gets an inference endpoint                     |
| [get_inference_endpoint_jobs](#get_inference_endpoint_jobs)     | Retrieves a list of an inference endpoint jobs |
| [create_inference_endpoint_job](#create_inference_endpoint_job) | Creates a new job                              |
| [get_inference_endpoint_job](#get_inference_endpoint_job)       | Retrieves a job in an inference endpoint       |
| [delete_inference_endpoint_job](#delete_inference_endpoint_job) | Deletes an inference endpoint job              |

## list_inference_endpoints

Gets the list of all inference endpoints

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/inference-endpoints`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |
| page              | int  | ❌       | The page number              |
| page_size         | int  | ❌       | The number of items per page |

**Return Type**

`InferenceEndpointsList`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoints(
    organization_name="bm3m3c1oqx1cbz9zmgggid",
    page=1997313670,
    page_size=11
)

print(result)
```

## get_inference_endpoint

Gets an inference endpoint

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}`

**Parameters**

| Name                    | Type | Required | Description                        |
| :---------------------- | :--- | :------- | :--------------------------------- |
| organization_name       | str  | ✅       | The unique organization name       |
| inference_endpoint_name | str  | ✅       | The unique inference endpoint name |

**Return Type**

`InferenceEndpoint`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint(
    organization_name="sedpgesuq9kpw3lnw7ag07-nla5",
    inference_endpoint_name="sed anim Lorem velit culpa"
)

print(result)
```

## get_inference_endpoint_jobs

Retrieves a list of an inference endpoint jobs

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs`

**Parameters**

| Name                    | Type | Required | Description                        |
| :---------------------- | :--- | :------- | :--------------------------------- |
| organization_name       | str  | ✅       | The unique organization name       |
| inference_endpoint_name | str  | ✅       | The unique inference endpoint name |
| page                    | int  | ❌       | The page number                    |
| page_size               | int  | ❌       | The number of items per page       |

**Return Type**

`InferenceEndpointJobList`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_jobs(
    organization_name="w7f4hj66c0",
    inference_endpoint_name="adipisicing",
    page=568449067,
    page_size=15
)

print(result)
```

## create_inference_endpoint_job

Creates a new job

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs`

**Parameters**

| Name                    | Type                                                                  | Required | Description                        |
| :---------------------- | :-------------------------------------------------------------------- | :------- | :--------------------------------- |
| request_body            | [CreateInferenceEndpointJob](../models/CreateInferenceEndpointJob.md) | ✅       | The request body.                  |
| organization_name       | str                                                                   | ✅       | The unique organization name       |
| inference_endpoint_name | str                                                                   | ✅       | The unique inference endpoint name |

**Return Type**

`InferenceEndpointJob`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateInferenceEndpointJob

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateInferenceEndpointJob(
    input="",
    metadata={},
    webhook="webhook"
)

result = sdk.inference_endpoints.create_inference_endpoint_job(
    request_body=request_body,
    organization_name="w7f4hj66c0",
    inference_endpoint_name="adipisicing"
)

print(result)
```

## get_inference_endpoint_job

Retrieves a job in an inference endpoint

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs/{inference_endpoint_job_id}`

**Parameters**

| Name                      | Type | Required | Description                        |
| :------------------------ | :--- | :------- | :--------------------------------- |
| organization_name         | str  | ✅       | The unique organization name       |
| inference_endpoint_name   | str  | ✅       | The unique inference endpoint name |
| inference_endpoint_job_id | str  | ✅       | The unique job id                  |

**Return Type**

`InferenceEndpointJob`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_job(
    organization_name="pcvy-5z9eei4",
    inference_endpoint_name="sunt occaecat",
    inference_endpoint_job_id="inference_endpoint_job_id"
)

print(result)
```

## delete_inference_endpoint_job

Deletes an inference endpoint job

- HTTP Method: `DELETE`
- Endpoint: `/organizations/{organization_name}/inference-endpoints/{inference_endpoint_name}/jobs/{inference_endpoint_job_id}`

**Parameters**

| Name                      | Type | Required | Description                        |
| :------------------------ | :--- | :------- | :--------------------------------- |
| organization_name         | str  | ✅       | The unique organization name       |
| inference_endpoint_name   | str  | ✅       | The unique inference endpoint name |
| inference_endpoint_job_id | str  | ✅       | The unique job id                  |

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.delete_inference_endpoint_job(
    organization_name="pcvy-5z9eei4",
    inference_endpoint_name="sunt occaecat",
    inference_endpoint_job_id="inference_endpoint_job_id"
)

print(result)
```
