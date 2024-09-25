```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="dcbh1",
    project_name="pdcapp3enb9gd2f4k49vviu53s67ckwwnxsd-gfjsmuxcljdg4t1zzyoj",
    container_group_name="vl2kuh4c67m3ae7qwlwipkdye-ad"
)

print(result)

```
