```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.start_container_group(
    organization_name="uh5upyur493wxwbxrj4xt9wfx07sgyz1fs97sfhtue78-54vdogp2qrcnt-8a",
    project_name="v7jhy3jn2rdf012fi7ouno3mk9",
    container_group_name="a4d0ajj5ajjquzeg-z3kvqxtnoxnlzhjhjt-8naw"
)

print(result)

```
