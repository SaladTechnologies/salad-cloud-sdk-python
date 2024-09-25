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

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |

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

result = sdk.webhook_secret_key.get_webhook_secret_key(organization_name="dyxdaqq1t3iwwpawdlk-78rt9bh26smkuf3v0nd2ropp")

print(result)
```

## update_webhook_secret_key

Updates the webhook secret key

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/webhook-secret-key`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_name | str  | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |

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

result = sdk.webhook_secret_key.update_webhook_secret_key(organization_name="dyxdaqq1t3iwwpawdlk-78rt9bh26smkuf3v0nd2ropp")

print(result)
```
