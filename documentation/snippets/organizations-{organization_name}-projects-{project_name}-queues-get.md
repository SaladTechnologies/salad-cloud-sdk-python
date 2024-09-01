```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queues(
    organization_name="tuw6h14q4yanz6jzs-93quj",
    project_name="zd-1kwc3qrr2qrta5-ma5yft7izvjtyvbpfqpzas8ys0rleuecgeq"
)

print(result)

```
