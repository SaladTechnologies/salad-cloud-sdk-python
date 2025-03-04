```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.delete_queue_job(
    organization_name="acme-corp",
    project_name="dev-env",
    queue_name="fifo-queue",
    queue_job_id="7dcd6922-50e9-4d56-89b5-91cde26f0211"
)

print(result)

```
