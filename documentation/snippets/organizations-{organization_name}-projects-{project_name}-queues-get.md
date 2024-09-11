```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queues(
    organization_name="v2321xyb8mgby4oaz0nnednrzwspo5e",
    project_name="uqcz1p0g5ye7j57a"
)

print(result)

```
