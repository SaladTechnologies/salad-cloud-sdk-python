```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="rywspw00apvowm2uk3ia7vi9jlaex78t718",
    project_name="ecf-7edommguhpzfl",
    container_group_name="ox6-1ksn8m"
)

print(result)

```
