```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.reallocate_container_group_instance(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="up72mwrutyouxr-mrzaprzs8bm0ocxuimiyjj4211pxc-t3uqn0dlhd4buflw2w",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
