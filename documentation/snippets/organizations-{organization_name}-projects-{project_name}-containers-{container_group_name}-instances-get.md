```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="i4i4ci3lnqp4d8my25qe5eucwfr0ni9ksw1jelhxjh",
    project_name="jfbvsusu0d8a1e8x94q0wsip8olrhfnnvkr7bgvgo196fb90srivpmzldjm59q",
    container_group_name="jk7y5mmm88"
)

print(result)

```
