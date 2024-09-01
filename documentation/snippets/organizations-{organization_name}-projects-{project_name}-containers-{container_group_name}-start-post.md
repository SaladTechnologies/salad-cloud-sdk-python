```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.start_container_group(
    organization_name="x1dy6hcwr9a5xaxeifh6e02xtma0zqz8asfuvjihhlkjxajbi3pwr9bnx",
    project_name="y7lm",
    container_group_name="l3q-oa3p3"
)

print(result)

```
