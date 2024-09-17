```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.delete_container_group(
    organization_name="bvf99pxxwtres8z9zwaod8ipjrui87jps52s0izl8d-g9wqh8bjg",
    project_name="d2tyh4q9ni9h81tilnlnf5i-r38a8vv5h3",
    container_group_name="it5rb91fzs3spaw4grzs1ulr7"
)

print(result)

```
