```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.delete_container_group(
    organization_name="ob3ca5hduqlb1uzytbhhukf1u0-ahl0b9oqfjj0q",
    project_name="x7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lx71",
    container_group_name="cif9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrm0urjjj5b9hbe2fr6f"
)

print(result)

```
