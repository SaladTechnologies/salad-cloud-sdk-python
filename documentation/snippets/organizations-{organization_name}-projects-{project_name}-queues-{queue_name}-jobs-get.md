```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="iugscfp5-4x1xl1-c1ax256",
    project_name="noy7vldsml0wxbxw",
    queue_name="sdtl98ziqb",
    page=477149090,
    page_size=12
)

print(result)

```
