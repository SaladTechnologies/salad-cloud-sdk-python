```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.inference_endpoints.list_inference_endpoints(
    organization_name="cy1l6xj-5vzihwp4ho850l3faynnuq71ru6y",
    page=1029360820,
    page_size=40
)

print(result)

```
