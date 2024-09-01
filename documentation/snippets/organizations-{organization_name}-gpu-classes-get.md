```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.organization_data.list_gpu_classes(organization_name="zd0f74r83g8t-3gf0nk0-ksf6kohlh6m-flte85e")

print(result)

```
