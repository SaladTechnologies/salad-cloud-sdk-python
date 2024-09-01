```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="qg6vce6y8gr9gth6qwq",
    project_name="hgk2",
    container_group_name="xxf9hw2fg7q6om9s6wkwjqmbzvl-xnxr-q14lm43yp"
)

print(result)

```
