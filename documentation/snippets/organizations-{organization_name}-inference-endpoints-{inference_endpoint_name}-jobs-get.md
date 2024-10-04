```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_jobs(
    organization_name="yg0u13rmnwb7eyumc25lm4prwopvwr-1961f",
    inference_endpoint_name="consectetur occaecat",
    page=355955712,
    page_size=39
)

print(result)

```
