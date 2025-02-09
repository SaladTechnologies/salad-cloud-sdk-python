```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.system_logs.get_system_logs(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="j6"
)

print(result)

```
