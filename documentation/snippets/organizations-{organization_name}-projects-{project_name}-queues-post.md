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
    name="ctrq4osv0lra1vqw6",
    display_name="snv",
    description="irure commodo ipsum veniam tempor"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="tuw6h14q4yanz6jzs-93quj",
    project_name="zd-1kwc3qrr2qrta5-ma5yft7izvjtyvbpfqpzas8ys0rleuecgeq"
)

print(result)

```
