```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateInferenceEndpointJob

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateInferenceEndpointJob(
    input="",
    metadata={},
    webhook="webhook"
)

result = sdk.inference_endpoints.create_inference_endpoint_job(
    request_body=request_body,
    organization_name="w7f4hj66c0",
    inference_endpoint_name="adipisicing"
)

print(result)

```
