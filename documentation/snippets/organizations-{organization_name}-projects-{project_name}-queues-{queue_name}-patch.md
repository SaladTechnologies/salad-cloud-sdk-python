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
    display_name="OpA2UXhB",
    description="ma"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="t6u-51xnolzq0i9u27d9qsg6qsygfges6",
    project_name="g1tktkoepudefqkf47dv60kqzd3q1wo8z4ukbuijty",
    queue_name="ff3kysrgbao"
)

print(result)

```
