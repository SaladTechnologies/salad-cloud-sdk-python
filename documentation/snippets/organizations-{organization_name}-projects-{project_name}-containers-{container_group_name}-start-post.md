```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.start_container_group(
    organization_name="z530zonqyj90ub",
    project_name="jreysxpqq7xwg32lxlhjn2dh8g4ria4k5sfrzd-3pdeog5yu4egwx3g9mbc",
    container_group_name="iyxmxxkxqv-nsi3p0ihren7kh3cozmla70br"
)

print(result)

```
