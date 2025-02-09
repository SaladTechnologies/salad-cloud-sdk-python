```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoints(
    organization_name="acme-corp",
    page=361997408,
    page_size=44
)

print(result)

```
