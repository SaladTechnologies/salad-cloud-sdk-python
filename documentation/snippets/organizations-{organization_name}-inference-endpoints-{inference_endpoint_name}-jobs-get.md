```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoint_jobs(
    organization_name="acme-corp",
    inference_endpoint_name="transcribe",
    page=1,
    page_size=1
)

print(result)

```
