```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import QueuePatch

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = QueuePatch(
    display_name="a83U5a",
    description="description"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env",
    queue_name="fifo-queue"
)

print(result)

```
