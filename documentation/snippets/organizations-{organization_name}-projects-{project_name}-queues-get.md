```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queues(
    organization_name="xtp82b9jzwqov1insghigvfq0donadhrrdqx-2redu46g7e",
    project_name="xk27gbnpmwk5xor49bk4ujk7"
)

print(result)

```
