```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_jobs(
    organization_name="bzx0y-i4o1cvulgdrx",
    inference_endpoint_name="minim",
    page=82661968,
    page_size=27
)

print(result)

```
