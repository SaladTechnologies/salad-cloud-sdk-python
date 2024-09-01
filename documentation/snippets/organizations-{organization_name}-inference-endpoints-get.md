```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoints(
    organization_name="bm3m3c1oqx1cbz9zmgggid",
    page=1997313670,
    page_size=11
)

print(result)

```
