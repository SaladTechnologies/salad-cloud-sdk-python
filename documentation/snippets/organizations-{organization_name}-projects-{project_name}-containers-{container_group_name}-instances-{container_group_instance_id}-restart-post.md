```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="kd79h7bg0vpngqc8hz5pxjwi7muqnmuuqsx3q3zm2hxkci5yv6kho",
    project_name="u5ljgqmbs6a7s",
    container_group_name="qmq3nj6oy8b2wpzbidnelidy9s6k9w",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
