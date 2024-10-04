```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.reallocate_container_group_instance(
    organization_name="sws1rwna83a3asu0izd6ugn07m5xpcp89lefemdke05z4s9d",
    project_name="ed2caksvlhpzmfccbh2v7dcapp3enb9gd2f4k49vviu53s5",
    container_group_name="xkwwnw",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
