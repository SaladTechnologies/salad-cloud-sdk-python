```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workload_errors.get_workload_errors(
    organization_name="e1hyb0xog4htqwzv2xifmedj8m3aft",
    project_name="ita8o56f6-ln3mgpj5ybc3o2jr6guahpm6a-9zm",
    container_group_name="in0mmtzaxq1g5d8jy220ol2mol23pv6c6zej"
)

print(result)

```
