# QuotasService

A list of all methods in the `QuotasService` service. Click on the method name to view detailed information about that method.

| Methods                   | Description                  |
| :------------------------ | :--------------------------- |
| [get_quotas](#get_quotas) | Gets the organization quotas |

## get_quotas

Gets the organization quotas

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/quotas`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |

**Return Type**

`Quotas`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.quotas.get_quotas(organization_name="b6n01-l4p5c2vk4867z")

print(result)
```
