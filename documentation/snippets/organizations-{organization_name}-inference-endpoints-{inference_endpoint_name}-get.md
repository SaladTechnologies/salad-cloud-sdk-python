```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint(
    organization_name="sedpgesuq9kpw3lnw7ag07-nla5",
    inference_endpoint_name="sed anim Lorem velit culpa"
)

print(result)

```
