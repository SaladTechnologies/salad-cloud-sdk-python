```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoints(
    organization_name="w5k7xmi1ci3kyzzon0m2iedxbj3f1dok1gz",
    page=744143038,
    page_size=88
)

print(result)

```
