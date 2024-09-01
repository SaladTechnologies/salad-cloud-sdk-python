```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.start_container_group(
    organization_name="jsq6na2w8d2wlvk-85d3jxhjhjigc",
    project_name="fv6oyiqlky7x2i-whfkhuex4ceacw4n3kgc3y89xb",
    container_group_name="a17zo0pyz6xi8-xbb6y7-prw04kcruh1moxld03jx91-zpoej07l0146fz"
)

print(result)

```
