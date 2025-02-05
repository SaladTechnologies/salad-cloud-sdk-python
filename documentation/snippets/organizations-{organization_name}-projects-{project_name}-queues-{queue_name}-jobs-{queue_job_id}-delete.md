```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.delete_queue_job(
    organization_name="hvm1ntcgljb71tp82b9jzwqov1insghigvfq0d",
    project_name="kadhrrdqx-2redu46g7e7nk1",
    queue_name="xbnpmwk5xor3",
    queue_job_id="queue_job_id"
)

print(result)

```
