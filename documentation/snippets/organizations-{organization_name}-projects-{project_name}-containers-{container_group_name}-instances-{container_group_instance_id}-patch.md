```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import ContainerGroupInstancePatch

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = ContainerGroupInstancePatch(
    deletion_cost=76724
)

result = sdk.container_groups.update_container_group_instance(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot",
    container_group_instance_id="db3a4591-efc3-46c0-b06a-3d820c0ec100"
)

print(result)

```
