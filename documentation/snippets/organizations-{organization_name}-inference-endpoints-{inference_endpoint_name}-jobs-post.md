```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateInferenceEndpointJob

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateInferenceEndpointJob(
    input="",
    metadata={},
    webhook="webhook"
)

result = sdk.inference_endpoints.create_inference_endpoint_job(
    request_body=request_body,
    organization_name="ux8b-38phiwjkfh3rhnvt4x30k5tue7r3q30x0anq7hd1fjfxgtq8ueh",
    inference_endpoint_name="inference_endpoint_name"
)

print(result)

```
