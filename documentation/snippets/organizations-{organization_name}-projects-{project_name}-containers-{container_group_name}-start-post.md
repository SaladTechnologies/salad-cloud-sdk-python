```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.start_container_group(
    organization_name="qv-nsi3p0ihren7kh3cozmla70bry",
    project_name="nwspw00apvowm2uk3ia7vi9jlaex78t719gjcf-7ed",
    container_group_name="jmguhpzfluex6-1ksn8mw9"
)

print(result)

```
