```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group_instance(
    organization_name="r3b4l8zryeh7q3m-b8y1cgkv",
    project_name="lw3mzmlm01jbt-edmy-frcr",
    container_group_name="jahux-5",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
