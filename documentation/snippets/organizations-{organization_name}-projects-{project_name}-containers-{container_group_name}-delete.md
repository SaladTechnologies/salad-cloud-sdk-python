```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.delete_container_group(
    organization_name="a147vxii7gy6-eg0n389rp",
    project_name="zcgtz8t87b",
    container_group_name="jonf9u1s785z-11dylxjw4966ge-9p6qcjc-qtefzoj09ev3nsih"
)

print(result)

```
