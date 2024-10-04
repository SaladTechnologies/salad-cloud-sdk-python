```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoints(
    organization_name="wtxd1j0ixuhfk-hdff3n3-hbtsigyh53bt0g4gjh8mcz4",
    page=121822981,
    page_size=37
)

print(result)

```
