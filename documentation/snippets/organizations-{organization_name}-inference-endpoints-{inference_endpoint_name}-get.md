```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint(
    organization_name="z8llajq25o",
    inference_endpoint_name="inference_endpoint_name"
)

print(result)

```
