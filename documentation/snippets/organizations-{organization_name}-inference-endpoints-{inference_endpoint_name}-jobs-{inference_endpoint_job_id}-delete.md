```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.cancel_inference_endpoint_job(
    organization_name="acme-corp",
    inference_endpoint_name="transcribe",
    inference_endpoint_job_id="2fc459a1-1c09-4a34-ade7-54d03fc51d6a"
)

print(result)

```
