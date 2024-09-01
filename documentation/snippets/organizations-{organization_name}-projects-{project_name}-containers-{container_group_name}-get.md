```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group(
    organization_name="hjn8ph-8qr9s",
    project_name="zpcs1c-85eq2giu1ly3ke1lk2gb3mqhp",
    container_group_name="obcxrd0mqez"
)

print(result)

```
