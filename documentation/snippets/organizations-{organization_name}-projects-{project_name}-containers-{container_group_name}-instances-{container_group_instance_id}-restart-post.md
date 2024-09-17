```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="k3eg40ckcze227v3cr47o2hb606akllh",
    project_name="dz9w578p05nje8zv80xtiift-dhcux3behoqegicbjgytvavm7ngiki6uxl76e",
    container_group_name="kwg5dgz5gi",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
