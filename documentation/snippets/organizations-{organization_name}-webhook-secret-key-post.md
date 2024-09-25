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
