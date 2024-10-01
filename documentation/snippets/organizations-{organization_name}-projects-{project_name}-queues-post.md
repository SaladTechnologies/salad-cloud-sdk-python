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
    name="wcaz2jbu5pfmpygxffsf4bh4e6",
    display_name="Ef",
    description="aute Ut nostrud veniam sint"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="rtxaydgbmb5wprcvb9628akhug9lnd3c0",
    project_name="p4bdb9jsi-f1xex70mdgjf5n-5ua-e28xyu9ujbls0vsz6xilo12xl52y9c177"
)

print(result)

```
