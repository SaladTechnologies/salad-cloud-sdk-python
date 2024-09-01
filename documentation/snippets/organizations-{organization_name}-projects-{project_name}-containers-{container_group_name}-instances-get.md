```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="r2ewwqmqzjxx4rgbkz9z0o",
    project_name="wsjwmyricvgcl-a",
    container_group_name="lfjbdzaim314b-agf7f3di5"
)

print(result)

```
