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

| Name                 | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |

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
    organization_name="x4hd7xmy53wgq8mpuy5k2wfbbzlhws5edt3sje",
    project_name="hug6abtk-ewjq1594j27m6u1whmqikj9f18pd",
    container_group_name="lq52i317o2r8pje-v4-ccp8q-329szw31h4fee236"
)

print(result)
```
