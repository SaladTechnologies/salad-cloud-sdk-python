```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="pb",
    project_name="dvb96iwcvlvvm1n",
    container_group_name="ngljb",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
