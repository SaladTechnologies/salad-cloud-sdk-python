```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_jobs(
    organization_name="w7f4hj66c0",
    inference_endpoint_name="adipisicing",
    page=568449067,
    page_size=15
)

print(result)

```
