```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.delete_queue_job(
    organization_name="zm-jv",
    project_name="tq26",
    queue_name="je5dpzbgsk8gvp",
    queue_job_id="queue_job_id"
)

print(result)

```
