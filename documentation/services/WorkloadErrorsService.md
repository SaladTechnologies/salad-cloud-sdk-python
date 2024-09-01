# WorkloadErrorsService

A list of all methods in the `WorkloadErrorsService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description              |
| :------------------------------------------ | :----------------------- |
| [get_workload_errors](#get_workload_errors) | Gets the workload errors |

## get_workload_errors

Gets the workload errors

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/errors`

**Parameters**

| Name                 | Type | Required | Description                     |
| :------------------- | :--- | :------- | :------------------------------ |
| organization_name    | str  | ✅       | The unique organization name    |
| project_name         | str  | ✅       | The unique project name         |
| container_group_name | str  | ✅       | The unique container group name |

**Return Type**

`WorkloadErrorList`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workload_errors.get_workload_errors(
    organization_name="wcmipcr4lct7sh6q8x591va-p0i2bmxlz92yn1jipe9lpa6ycl1ukd",
    project_name="k-gt-dvmb-gmo",
    container_group_name="wg"
)

print(result)
```
