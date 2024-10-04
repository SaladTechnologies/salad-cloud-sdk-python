```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateQueueJob

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateQueueJob(
    input="",
    metadata={},
    webhook="webhook"
)

result = sdk.queues.create_queue_job(
    request_body=request_body,
    organization_name="wcaz2jbu5pfmpygxffsf4bh4e6",
    project_name="dzh9lv6afpamv8cx0x6",
    queue_name="s9f4ikmr0j6c3n18n4djttkqmgzb46dd5wogzrfe2pq12s2"
)

print(result)

```
