```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import InferenceEndpointJobPrototype

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = InferenceEndpointJobPrototype(
    input="",
    metadata={},
    webhook_url="https://webhook.example.com/events"
)

result = sdk.inference_endpoints.create_inference_endpoint_job(
    request_body=request_body,
    organization_name="acme-corp",
    inference_endpoint_name="transcribe"
)

print(result)

```
