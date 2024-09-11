```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="x2hb606akllhe-z9w578p05ni",
    project_name="czv80xtiift-dhcux3behoqegicbjgytvavm7ngiki6uxl76eoewg5dgz5g",
    container_group_name="f3mzshp",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
