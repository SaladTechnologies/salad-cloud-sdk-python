```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.restart_container_group_instance(
    organization_name="q4bvcc9w5lcg",
    project_name="ar4nzwg42bty8xw-dowooq-ycquvtr7pp0h2y24hkt0ps",
    container_group_name="j0s47o7jvc3kavg47t-viw2vz0xrxk6qarbrczxkh6",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
