```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="kjhy3jn2rdf012fi7ouno3mk-ax4d0ajj5ajjquzeg-z3kvqxtnoxnlzhi",
    project_name="ft-8nawc40o0gqev-m",
    container_group_name="jpy8af-s7rq68p2lenu"
)

print(result)

```
