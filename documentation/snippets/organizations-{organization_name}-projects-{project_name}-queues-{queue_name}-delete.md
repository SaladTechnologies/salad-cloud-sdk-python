```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.delete_queue(
    organization_name="g1bq27ohe5dpzbgsk8gvpuhecson4k2eclxss3",
    project_name="wtxd1j0ixuhfk-hdff3n3-hbtsigyh53bt0g4gjh8mcz4",
    queue_name="bnkfiyt3k5ke3wy-5gl1809r"
)

print(result)

```
