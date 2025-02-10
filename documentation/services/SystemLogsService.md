# SystemLogsService

A list of all methods in the `SystemLogsService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description          |
| :---------------------------------- | :------------------- |
| [get_system_logs](#get_system_logs) | Gets the System Logs |

## get_system_logs

Gets the System Logs

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/projects/{project_name}/containers/{container_group_name}/system-logs`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name    | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |
| project_name         | str  | ✅       | Your project name. This represents a collection of related SaladCloud resources. The project must be created before using the API.                                                                                                                  |
| container_group_name | str  | ✅       | The unique container group name                                                                                                                                                                                                                     |

**Return Type**

`SystemLogList`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.system_logs.get_system_logs(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="iywssc78i61j8diudajp-56rw2k19rew4p"
)

print(result)
```
