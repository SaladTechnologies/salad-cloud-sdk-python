```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.list_container_groups(
    organization_name="dj0q7z7dvdopv2czf",
    project_name="c1zrufxgh"
)

print(result)

```
