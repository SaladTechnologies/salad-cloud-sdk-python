```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group_instance(
    organization_name="bsf7v",
    project_name="ulau11f5g2zdmdpxhrfzhv7x3dhck87lv8-z-v",
    container_group_name="efzk8ea2roe6yryt0-t1885dp762ut0igkfak4jbmum3tb50ov",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
