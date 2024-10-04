```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group_instance(
    organization_name="a09xnu6-fkv3",
    project_name="ca4ydy-pi16e4ddle58fi8u9w2qgnsgj7cn",
    container_group_name="b4p90a72aagy0fz",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
