```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.get_container_group(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot"
)

print(result)

```
