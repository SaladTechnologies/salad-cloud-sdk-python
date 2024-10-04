```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.webhook_secret_key.get_webhook_secret_key(organization_name="mouv4w914sp420zyiuo43jexocjzq6rnxf04dqmccakipx9g3a72svbj")

print(result)

```
