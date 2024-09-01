# WebhookSecretKeyService

A list of all methods in the `WebhookSecretKeyService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                    |
| :------------------------------------------------------ | :----------------------------- |
| [get_webhook_secret_key](#get_webhook_secret_key)       | Gets the webhook secret key    |
| [update_webhook_secret_key](#update_webhook_secret_key) | Updates the webhook secret key |

## get_webhook_secret_key

Gets the webhook secret key

- HTTP Method: `GET`
- Endpoint: `/organizations/{organization_name}/webhook-secret-key`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |

**Return Type**

`WebhookSecretKey`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.webhook_secret_key.get_webhook_secret_key(organization_name="jssz72m10sc7zwl8ppw0zbzrujz78gkm2ls07")

print(result)
```

## update_webhook_secret_key

Updates the webhook secret key

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/webhook-secret-key`

**Parameters**

| Name              | Type | Required | Description                  |
| :---------------- | :--- | :------- | :--------------------------- |
| organization_name | str  | ✅       | The unique organization name |

**Return Type**

`WebhookSecretKey`

**Example Usage Code Snippet**

```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.webhook_secret_key.update_webhook_secret_key(organization_name="jssz72m10sc7zwl8ppw0zbzrujz78gkm2ls07")

print(result)
```
