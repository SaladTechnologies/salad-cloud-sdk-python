```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queues(
    organization_name="gcmqvx5-larlezt8ks00ar9f8kfq524njjzfmn5dis4gk",
    project_name="x9ql9z"
)

print(result)

```
