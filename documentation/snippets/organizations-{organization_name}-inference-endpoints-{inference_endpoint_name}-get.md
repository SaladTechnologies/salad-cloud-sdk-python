```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint(
    organization_name="v7b03k36nalu2j2kv",
    inference_endpoint_name="culpa dolor anim ve"
)

print(result)

```
