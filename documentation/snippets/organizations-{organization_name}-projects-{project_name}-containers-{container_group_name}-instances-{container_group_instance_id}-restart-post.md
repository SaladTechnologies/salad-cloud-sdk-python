```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="elwyv8cc9z7auxq8gmm5tqiz3fh3lty-n963c-nzs6rcc8qglueef-fdu",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
