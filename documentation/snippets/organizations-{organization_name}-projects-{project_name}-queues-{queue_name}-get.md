```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.get_queue(
    organization_name="inu8izbgz",
    project_name="ynu6-fkv4dta4ydy-pi16e4ddle58fi8u9w2qgnsg",
    queue_name="gcnci4p90a72aagy0f001ws1rwna83a3asu0izd6ugn07m5xpcp89lefe"
)

print(result)

```
