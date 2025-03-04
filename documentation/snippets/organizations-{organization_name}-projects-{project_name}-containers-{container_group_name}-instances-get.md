```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="gd6c-o-5jwj2ocq-dvadg2cp1l-tkh9w1m"
)

print(result)

```
