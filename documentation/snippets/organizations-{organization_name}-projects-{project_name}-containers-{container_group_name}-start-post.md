```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.start_container_group(
    organization_name="on6upv4ibz",
    project_name="bp3skoan866qk08-4",
    container_group_name="vmvb7kyluk2iobnx9by712swz71xj38i4"
)

print(result)

```
