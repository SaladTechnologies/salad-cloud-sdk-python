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
    display_name="wfoWE",
    description="aliqua in sit"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="ljj6uqmy01xsg7k5n8fhpr0uia1-28ec6ahk-1s6u-51xn",
    project_name="jzq0i9u27d9qsg6qsygfg",
    queue_name="d7iy1tktkoepudefqkf47dv60kqzd3q1v"
)

print(result)

```
