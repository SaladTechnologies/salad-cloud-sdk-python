# OrganizationDataService

A list of all methods in the `OrganizationDataService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description          |
| :------------------------------------ | :------------------- |
| [list_gpu_classes](#list_gpu_classes) | List the GPU Classes |

## list_gpu_classes

List the GPU Classes

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/gpu-classes`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |

**Return Type**

`GpuClassesList`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.organization_data.list_gpu_classes(organization_name="zd0f74r83g8t-3gf0nk0-ksf6kohlh6m-flte85e")

print(result)
```
