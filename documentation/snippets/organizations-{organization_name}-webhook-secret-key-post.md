```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.webhook_secret_key.update_webhook_secret_key(organization_name="o1yeste00ep44ion-cfbuqm7ankfh00qxjgqhc7gu8nezs4j9l1xu8i")

print(result)

```
