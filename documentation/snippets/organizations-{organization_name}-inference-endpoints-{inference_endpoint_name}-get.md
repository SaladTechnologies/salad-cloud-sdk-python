```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint(
    organization_name="uzp1dyfm2yp4-lxa27tl0fwms3fu3myo74a99jr6ouv4w8",
    inference_endpoint_name="aute Ut reprehenderit occaecat sed"
)

print(result)

```
