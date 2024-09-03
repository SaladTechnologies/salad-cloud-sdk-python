```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_jobs(
    organization_name="trzfoq1p77wk9jgwxjp56dzbnwtbgowklqt1wsbe00",
    inference_endpoint_name="ut officia ut",
    page=1653138765,
    page_size=76
)

print(result)

```
