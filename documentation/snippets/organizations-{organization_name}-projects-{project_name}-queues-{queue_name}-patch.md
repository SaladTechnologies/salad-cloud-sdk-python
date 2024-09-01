```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import UpdateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateQueue(
    display_name="tgkuNWMcC",
    description="in"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="j0404lk6i34cuer",
    project_name="ekiabi4sbb23l56oq87j1v",
    queue_name="w4hdchyg-8n5glaql3-539c26ytntnk7-le269faihpgelqal6jc72"
)

print(result)

```
