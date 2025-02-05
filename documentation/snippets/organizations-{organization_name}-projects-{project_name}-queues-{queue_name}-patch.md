```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import UpdateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = UpdateQueue(
    display_name="2E4g",
    description="description"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="inu8izbgz",
    project_name="ynu6-fkv4dta4ydy-pi16e4ddle58fi8u9w2qgnsg",
    queue_name="gcnci4p90a72aagy0f001ws1rwna83a3asu0izd6ugn07m5xpcp89lefe"
)

print(result)

```
