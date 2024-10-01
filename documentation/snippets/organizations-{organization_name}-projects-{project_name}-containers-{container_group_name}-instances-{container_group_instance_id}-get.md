```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group_instance(
    organization_name="b0up7kyr7vabeivb96iwcvlvvm1n",
    project_name="ngljb",
    container_group_name="xtp82b9jzwqov1insghigvfq0donadhrrdqx-2redu46g7e",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
