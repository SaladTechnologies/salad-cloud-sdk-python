```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_jobs(
    organization_name="ux8b-38phiwjkfh3rhnvt4x30k5tue7r3q30x0anq7hd1fjfxgtq8ueh",
    inference_endpoint_name="inference_endpoint_name",
    page=508294663,
    page_size=31
)

print(result)

```
