```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.get_inference_endpoint_job(
    organization_name="fa9p9or6f6b78k5l055jui8tmpngms0ir5zg3ixfzqkola94rkm",
    inference_endpoint_name="mollit",
    inference_endpoint_job_id="inference_endpoint_job_id"
)

print(result)

```
