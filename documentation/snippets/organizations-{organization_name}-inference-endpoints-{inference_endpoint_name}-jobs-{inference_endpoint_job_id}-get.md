```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_job(
    organization_name="s04w2crlogjmfdcc56apm9zbbx488p3ma8ymve3kv7u5j1tuskgp-t61s33ubq",
    inference_endpoint_name="sint ea",
    inference_endpoint_job_id="inference_endpoint_job_id"
)

print(result)

```
