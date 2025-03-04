```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="acme-corp",
    project_name="dev-env",
    queue_name="fifo-queue",
    page=1,
    page_size=1
)

print(result)

```
