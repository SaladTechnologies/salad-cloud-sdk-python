```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint(
    organization_name="r3ca1qhgg3f8sedhivpq69pz1fv6p6td3lk58q-xi9e71",
    inference_endpoint_name="ex"
)

print(result)

```
