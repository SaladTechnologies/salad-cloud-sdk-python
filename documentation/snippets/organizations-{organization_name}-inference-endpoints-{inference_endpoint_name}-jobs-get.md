```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_jobs(
    organization_name="o5xa3fo8vph2o1f-37ajjw041g16mvzbwxaa3c0u0co",
    inference_endpoint_name="nulla do",
    page=1108363256,
    page_size=2
)

print(result)

```
