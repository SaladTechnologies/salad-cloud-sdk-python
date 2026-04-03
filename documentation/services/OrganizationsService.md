# OrganizationsService

A list of all methods in the `OrganizationsService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                          |
| :-------------------------------------------- | :--------------------------------------------------- |
| [get_cpu_availability](#get_cpu_availability) | Gets the CPU availability for the given organization |
| [get_gpu_availability](#get_gpu_availability) | Gets the GPU availability for the given organization |

## get_cpu_availability

Gets the CPU availability for the given organization

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/availability/sce-cpu-availability`

**Parameters**

| Name              | Type                                                              | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [CpuAvailabilityPrototype](../models/CpuAvailabilityPrototype.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | str                                                               | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |

**Return Type**

`CpuAvailability`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CpuAvailabilityPrototype

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CpuAvailabilityPrototype(
    country_codes=[
        "af"
    ],
    cpu=4,
    memory=8192,
    storage_amount=1000000000
)

result = sdk.organizations.get_cpu_availability(
    request_body=request_body,
    organization_name="acme-corp"
)

print(result)
```

## get_gpu_availability

Gets the GPU availability for the given organization

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/availability/sce-gpu-availability`

**Parameters**

| Name              | Type                                                              | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [GpuAvailabilityPrototype](../models/GpuAvailabilityPrototype.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | str                                                               | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |

**Return Type**

`GpuAvailability`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import GpuAvailabilityPrototype

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = GpuAvailabilityPrototype(
    country_codes=[
        "af"
    ],
    cpu=4,
    gpu_classes=[
        "gpu_classes"
    ],
    memory=8192,
    storage_amount=1000000000
)

result = sdk.organizations.get_gpu_availability(
    request_body=request_body,
    organization_name="acme-corp"
)

print(result)
```
