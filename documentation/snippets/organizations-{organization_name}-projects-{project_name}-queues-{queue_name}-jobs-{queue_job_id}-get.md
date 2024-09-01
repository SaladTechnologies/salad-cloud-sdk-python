```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.get_queue_job(
    organization_name="q5amdp8n95tm7sbm4-h-l-za21p3dtwrf8h51jcaivs9xc",
    project_name="nhu27mdjh418v3ixyidy7jsx-nnjlyt7-bhj1c1wox",
    queue_name="tszyoxkrcz6v9wz35jltvo0g-6z9z",
    queue_job_id="queue_job_id"
)

print(result)

```
