```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.inference_endpoints.delete_inference_endpoint_job(
    organization_name="v0jo001xz6w2uhgmhtgvpqzhztmaqawqn92-rig0bznv-21cb7tj-hp2ecbvldq",
    inference_endpoint_name="elit sint",
    inference_endpoint_job_id="inference_endpoint_job_id"
)

print(result)

```
