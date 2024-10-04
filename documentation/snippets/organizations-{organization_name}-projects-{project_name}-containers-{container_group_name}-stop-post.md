```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="jpqhlkkgd",
    project_name="a9h5upyur493wxwbxrj4xt9wfx07sgyz1fs97sfhtue78-54vd",
    container_group_name="jp2qrcnt-8a3"
)

print(result)

```
