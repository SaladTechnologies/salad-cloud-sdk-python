```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateQueue(
    name="ho4d79h7bg0vpngqc8hz5pxjwi",
    display_name="IWPKHVWPTc",
    description="aliqua id nostrud"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="xtp82b9jzwqov1insghigvfq0donadhrrdqx-2redu46g7e",
    project_name="xk27gbnpmwk5xor49bk4ujk7"
)

print(result)

```
