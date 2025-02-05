```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="ea39h5t",
    project_name="kur493wxwbxrj4xt9wfx07sgyz1fs97sfhtue78-54",
    container_group_name="oogp2qrc",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
