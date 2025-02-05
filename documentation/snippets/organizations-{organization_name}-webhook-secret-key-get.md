```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.webhook_secret_key.get_webhook_secret_key(organization_name="aswqmq3nj6oy8b2wpzbidnelidy9s6k9wystxaydgbmb5wprcvb9628akh")

print(result)

```
