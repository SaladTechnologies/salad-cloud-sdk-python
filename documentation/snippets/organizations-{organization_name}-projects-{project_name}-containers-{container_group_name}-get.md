```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group(
    organization_name="oji7lyvxb3ca5hc",
    project_name="olb1uzytbhhukf1u0-ahl0b9oqfjj",
    container_group_name="s7z7dvdopv2czgde1zrufxgiv5tp-j"
)

print(result)

```
