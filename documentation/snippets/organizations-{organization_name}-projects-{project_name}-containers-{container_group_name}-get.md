```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group(
    organization_name="xpjrui87jps52s0iy",
    project_name="hd-g9wqh8bjget2tyh4q9ni9h81tilnlnf5i-r38a8vv5h4lnt5rb91fzs2",
    container_group_name="naw4grzs1ulr8elj96ymws1tye0"
)

print(result)

```
