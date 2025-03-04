```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateQueue(
    name="name",
    display_name="QPrF.myB W",
    description="description"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env"
)

print(result)

```
