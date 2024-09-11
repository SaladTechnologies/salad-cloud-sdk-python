```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.delete_queue_job(
    organization_name="qfyxrcpjzz",
    project_name="u68mnowwsycakrj2ndjibysiw6",
    queue_name="qw8v11op7e4dq1ckmwu5v289qp5d1ln00phm2",
    queue_job_id="queue_job_id"
)

print(result)

```
