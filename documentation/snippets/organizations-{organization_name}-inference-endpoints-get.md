```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoints(
    organization_name="wg1umdxtc9fte8osib-e-5ux2vsmrhjjt13u7q3pryxxnm",
    page=756148233,
    page_size=66
)

print(result)

```
