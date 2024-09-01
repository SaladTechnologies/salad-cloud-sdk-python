```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.get_queue_job(
    organization_name="vxqcbddvaoe06qhpuoplm89wi2894q9cpfigd95ewlngasgx2e93zxei",
    project_name="iri0-iro9w0j3jvvgj2awj6-0ivo86",
    queue_name="e7zccce0i4ccb53k4gtsp-47yvqix8go1831z2sf2i8",
    queue_job_id="queue_job_id"
)

print(result)

```
