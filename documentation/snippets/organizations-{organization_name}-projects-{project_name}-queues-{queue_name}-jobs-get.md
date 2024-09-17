```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="bodal6rzqd6z",
    project_name="tw1si55p9gl6eb4zglez6wd",
    queue_name="sp8h2",
    page=648177408,
    page_size=33
)

print(result)

```
